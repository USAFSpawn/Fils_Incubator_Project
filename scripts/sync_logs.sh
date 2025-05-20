#!/bin/bash

# 🛠 Cloud Log Sync - Google Drive & OneDrive

echo "🚀 Setting Up Cloud Sync for Logs..."

# Install RClone
sudo apt install -y rclone

# Configure RClone (User selects service manually)
echo "📡 Configuring RClone..."
rclone config

# User Selection: Google Drive or OneDrive
echo "🔧 Select Cloud Destination (GoogleDrive / OneDrive):"
read CLOUD_OPTION

# Define Sync Frequency (Minutes)
echo "⌛ Enter sync frequency (minutes):"
read SYNC_FREQUENCY

# Set Sync Paths
LOG_PATH="/logs/"
REMOTE_PATH="$CLOUD_OPTION:/IncubatorLogs"

# Create Cron Job for Sync
(crontab -l 2>/dev/null; echo "*/$SYNC_FREQUENCY * * * * rclone sync $LOG_PATH $REMOTE_PATH") | crontab -

echo "✅ Cloud Sync Configured! Logs will sync every $SYNC_FREQUENCY minutes to $CLOUD_OPTION."
