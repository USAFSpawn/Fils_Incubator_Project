# 📢 SMS & Email Alerts Setup Guide

This guide walks you through configuring **Twilio (SMS)** and **SMTP (Email)** alerts for the incubator.

## **🔧 1️⃣ Twilio Setup (SMS Alerts)**
1. **Sign Up for Twilio** [here](https://www.twilio.com/)
2. **Get Credentials**:
   - Account SID
   - Auth Token
   - Twilio Phone Number
3. **Add Credentials to `config/alerts.env`**:
   ```plaintext
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH=your_twilio_auth_token
   TWILIO_PHONE=+11234567890
