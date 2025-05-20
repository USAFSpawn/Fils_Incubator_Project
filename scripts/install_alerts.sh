#!/bin/bash

# 🛠 Incubator Alert System Setup Script

echo "🚀 Installing Twilio & SMTP Dependencies..."

# Install Required Python Packages
pip3 install twilio smtplib email-validator

# Set Up Twilio Credentials
echo "🔧 Configuring Twilio..."
TWILIO_SID="your_twilio_sid_here"
TWILIO_AUTH="your_twilio_auth_token_here"
TWILIO_PHONE="+11234567890"

# Set Up Email (Gmail Example)
EMAIL_SERVER="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USER="your_email@gmail.com"
EMAIL_PASS="your_email_password_here"

# Store credentials in `config/alerts.env`
echo "TWILIO_SID=$TWILIO_SID" >> config/alerts.env
echo "TWILIO_AUTH=$TWILIO_AUTH" >> config/alerts.env
echo "TWILIO_PHONE=$TWILIO_PHONE" >> config/alerts.env
echo "EMAIL_SERVER=$EMAIL_SERVER" >> config/alerts.env
echo "EMAIL_PORT=$EMAIL_PORT" >> config/alerts.env
echo "EMAIL_USER=$EMAIL_USER" >> config/alerts.env
echo "EMAIL_PASS=$EMAIL_PASS" >> config/alerts.env

echo "✅ Twilio & Email Alerts Configured!"
