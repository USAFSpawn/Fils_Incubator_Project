# 🐣 Fils_Incubator_Project - Web Server (web_server.py)
# This script provides a Flask-based web dashboard for monitoring and managing the incubator.
# ✅ Provides live monitoring & incubator control via Flask API.
# ✅ Integrates SMS & Email Alerts for temperature/humidity threshold violations.
# ✅ Supports real-time data visualization for incubation tracking.

import json
import sqlite3
import smtplib
from email.mime.text import MIMEText
import paho.mqtt.client as mqtt
from twilio.rest import Client
from flask import Flask, jsonify, render_template, request

# 🔧 Load Configuration Settings from JSON
CONFIG_FILE = "../config/settings.json"
DATABASE_FILE = "../logs/incubator_data.db"
ALERTS_CONFIG_FILE = "../config/alerts.env"

def load_settings():
    """Loads system configuration from settings.json."""
    with open(CONFIG_FILE, "r") as config_file:
        return json.load(config_file)

settings = load_settings()

# 📡 MQTT Configuration
MQTT_BROKER = settings["MQTT"]["BROKER"]
MQTT_PORT = settings["MQTT"]["PORT"]
MQTT_TOPICS = settings["MQTT"]["TOPICS"]

# 📢 Load Alert Credentials
alert_creds = {}
with open(ALERTS_CONFIG_FILE, "r") as env_file:
    for line in env_file:
        key, value = line.strip().split("=")
        alert_creds[key] = value

# Initialize Flask App
app = Flask(__name__)

# 📡 MQTT Client Setup
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# 🔥 Route: Home Dashboard
@app.route("/")
def dashboard():
    """Render the main dashboard with live sensor data & settings editor."""
    temp, humidity = read_latest_sensor_data()
    return render_template("dashboard.html", temperature=temp, humidity=humidity, settings=settings)

# 📊 Route: Fetch Latest Sensor Data
@app.route("/api/sensors")
def sensor_api():
    """Return the latest temperature and humidity data in JSON format."""
    temp, humidity = read_latest_sensor_data()

    if settings["ALERTS"]["ENABLED"]:
        check_alerts(temp, humidity)

    return jsonify({"temperature": temp, "humidity": humidity})

# 📡 Route: Send MQTT Command
@app.route("/api/command/<action>")
def send_mqtt_command(action):
    """Send a command to the incubator via MQTT."""
    if action in ["start", "stop", "reset"]:
        mqtt_client.publish(MQTT_TOPICS["COMMANDS"], action)
        return jsonify({"status": "success", "message": f"Command '{action}' sent."})
    else:
        return jsonify({"status": "error", "message": "Invalid command."}), 400

# 📝 Route: Update settings.json
@app.route("/api/update-settings", methods=["POST"])
def update_settings():
    """Modify incubator settings based on user input."""
    try:
        new_settings = request.json

        # Validate input before updating
        temp_high = new_settings["ALERTS"].get("TEMP_HIGH_THRESHOLD_FAHRENHEIT", None)
        temp_low = new_settings["ALERTS"].get("TEMP_LOW_THRESHOLD_FAHRENHEIT", None)
        if temp_high and temp_low and temp_low >= temp_high:
            return jsonify({"status": "error", "message": "Low threshold must be lower than high threshold"}), 400

        # Write to settings.json
        with open(CONFIG_FILE, "w") as config_file:
            json.dump(new_settings, config_file, indent=4)

        global settings
        settings = new_settings  # Reload active configuration

        return jsonify({"status": "success", "message": "Settings updated successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 💾 Function: Read Latest Sensor Data from SQLite
def read_latest_sensor_data():
    """Fetch the most recent sensor readings from the database."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT temp, humidity FROM incubator ORDER BY timestamp DESC LIMIT 1")
    data = c.fetchone()
    conn.close()

    return data if data else (99.5, 55.0)

# 📢 Function: Trigger SMS & Email Alerts
def check_alerts(temp, humidity):
    """Triggers alerts if temperature/humidity are outside defined safe ranges."""
    alerts = settings["ALERTS"]

    temp_alert = temp < alerts["TEMP_LOW_THRESHOLD_FAHRENHEIT"] or temp > alerts["TEMP_HIGH_THRESHOLD_FAHRENHEIT"]
    humidity_alert = humidity < alerts["HUMIDITY_LOW_THRESHOLD_PERCENT"] or humidity > alerts["HUMIDITY_HIGH_THRESHOLD_PERCENT"]

    if temp_alert or humidity_alert:
        message = f"🚨 Alert! Incubator readings outside safe range:\nTemperature: {temp}°F\nHumidity: {humidity}%"

        if alerts["SMS_ENABLED"]:
            send_sms(message)
        if alerts["EMAIL_ENABLED"]:
            send_email(message)

# 📡 Function: Send SMS via Twilio
def send_sms(message):
    """Sends an SMS notification using Twilio."""
    client = Client(alert_creds["TWILIO_SID"], alert_creds["TWILIO_AUTH"])
    client.messages.create(body=message, from_=alert_creds["TWILIO_PHONE"], to=settings["ALERTS"]["SMS_NUMBER"])

# 📧 Function: Send Email Alert
def send_email(message):
    """Sends an email alert using SMTP."""
    msg = MIMEText(message)
    msg["Subject"] = "🚨 Incubator Alert"
    msg["From"] = alert_creds["EMAIL_USER"]
    msg["To"] = settings["ALERTS"]["EMAIL_RECIPIENT"]

    server = smtplib.SMTP(alert_creds["EMAIL_SERVER"], int(alert_creds["EMAIL_PORT"]))
    server.starttls()
    server.login(alert_creds["EMAIL_USER"], alert_creds["EMAIL_PASS"])
    server.sendmail(alert_creds["EMAIL_USER"], settings["ALERTS"]["EMAIL_RECIPIENT"], msg.as_string())
    server.quit()

# 🔧 Main Execution
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=settings["LOGGING"]["DEBUG_MODE"])