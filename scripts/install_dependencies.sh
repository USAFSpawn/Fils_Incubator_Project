#!/bin/bash

echo "🚀 Installing dependencies for Incubator System..."

# Update & install essential packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip sqlite3 mosquitto mosquitto-clients rclone

# Install Python libraries
pip3 install flask paho-mqtt twilio smtplib email-validator gpiozero chart.js

echo "✅ Dependencies installed successfully!"
