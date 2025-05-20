# 🐣 Fils_Incubator_Project - Web Server (web_server.py)
# This script provides a Flask-based web dashboard for monitoring and managing the incubator.
# ✅ Displays Live Sensor Data
# ✅ Allows Remote MQTT Control
# ✅ Enables Editing of settings.json via Web UI
# ✅ Supports Real-time Graph Updates using Chart.js

import json
import sqlite3
import paho.mqtt.client as mqtt
from flask import Flask, jsonify, render_template, request

# 🔧 Load Configuration Settings from JSON
CONFIG_FILE = "../config/settings.json"
DATABASE_FILE = "../logs/incubator_data.db"

# Function to Load Settings
def load_settings():
    with open(CONFIG_FILE, "r") as config_file:
        return json.load(config_file)

settings = load_settings()

# MQTT Configuration
MQTT_BROKER = settings["MQTT"]["BROKER"]
MQTT_PORT = settings["MQTT"]["PORT"]
MQTT_TOPICS = settings["MQTT"]["TOPICS"]

# Initialize Flask App
app = Flask(__name__)

# 📡 MQTT Client Setup
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# 🔥 Route: Home Dashboard
@app.route("/")
def dashboard():
    """Render the main dashboard with live sensor data and settings editor."""
    temp, humidity = read_latest_sensor_data()
    return render_template("dashboard.html", temperature=temp, humidity=humidity, settings=settings)

# 📊 Route: Fetch Latest Sensor Data
@app.route("/api/sensors")
def sensor_api():
    """Return the latest temperature and humidity data in JSON format."""
    temp, humidity = read_latest_sensor_data()
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
        if "ADAPTIVE_CLIMATE_CONTROL" in new_settings:
            temp_target = new_settings["ADAPTIVE_CLIMATE_CONTROL"].get("TEMPERATURE_TARGET_FAHRENHEIT", None)
            if temp_target and not (80 <= temp_target <= 105):  # Safe incubation range
                return jsonify({"status": "error", "message": "Invalid temperature range"}), 400

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

    # Return default values if no data exists
    return data if data else (99.5, 55.0)

# 📈 Route: Fetch Historical Sensor Data for Graphs
@app.route("/api/history")
def fetch_history():
    """Return historical sensor data for graph visualization."""
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT timestamp, temp, humidity FROM incubator ORDER BY timestamp DESC LIMIT 30")
    data = [{"timestamp": row[0], "temperature": row[1], "humidity": row[2]} for row in c.fetchall()]
    conn.close()

    return jsonify(data)

# 🔧 Main Execution
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=settings["LOGGING"]["DEBUG_MODE"])