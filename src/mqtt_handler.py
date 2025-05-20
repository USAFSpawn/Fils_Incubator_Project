# 🐣 MQTT Handler - Manages real-time sensor data exchange

import paho.mqtt.client as mqtt

BROKER = "mqtt.local"
PORT = 1883
TOPIC = "incubator/temp"

def on_message(client, userdata, msg):
    """Handles incoming MQTT messages."""
    print(f"Received message: {msg.payload.decode()}")

client = mqtt.Client()
client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.on_message = on_message

client.loop_start()
