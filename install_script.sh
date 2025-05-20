#!/bin/bash

# 🛠 Fils_Incubator_Project - Installation Script
# ✅ Automates setup for Python dependencies, configurations, and service startup.

echo "🚀 Starting Incubator System Installation..."

# Update & Install Required Packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip sqlite3 mosquitto mosquitto-clients

# Install Python Dependencies
pip3 install -r requirements.txt

# Set Up Default Configuration (if missing)
CONFIG_FILE="config/settings.json"
DEFAULT_CONFIG="config/default_settings.json"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "🔧 Copying default settings.json..."
    cp "$DEFAULT_CONFIG" "$CONFIG_FILE"
fi

# Ensure Web Server Starts on Boot
echo "📡 Configuring Web Server..."
sudo cp system/web_server.service /etc/systemd/system/
sudo systemctl enable web_server
sudo systemctl start web_server

echo "✅ Installation Complete! Run 'python3 src/incubator.py' to start the system."
