# 🛠 Fils_Incubator_Project - Setup Instructions

This document provides **step-by-step installation instructions** to set up the **Raspberry Pi-based incubator system**, ensuring seamless operation of temperature monitoring, egg turning, data logging, and remote access.

---

## **1️⃣ System Requirements**
To ensure smooth operation, your setup should meet the following requirements:

### **Hardware Requirements**
- ✅ **Raspberry Pi 4B (Recommended)** or **Raspberry Pi Zero 2 W**
- ✅ **MicroSD Card (32GB or higher)**
- ✅ **Temperature & Humidity Sensors (SHT4x or DHT22)**
- ✅ **Egg Turner Motor (Servo MG995 or Stepper NEMA 17)**
- ✅ **12V Heater Pad & Humidifier**
- ✅ **Cooling Fan for Air Circulation**
- ✅ **PiCamera for Live Monitoring**

### **Software Requirements**
- ✅ **Raspberry Pi OS Lite (Recommended)**
- ✅ **Python 3.9+**
- ✅ **Flask (For Web Interface)**
- ✅ **MQTT Broker (For IoT Communication)**
- ✅ **SQLite (For Data Logging)**

---

## **2️⃣ Setting Up Raspberry Pi OS**
### **Flash Raspberry Pi OS Lite**
1. Download **Raspberry Pi Imager** from [here](https://www.raspberrypi.org/software/).
2. Flash **Raspberry Pi OS Lite** onto the MicroSD card.
3. Insert the MicroSD card into your Raspberry Pi and **connect power**.
4. Enable **SSH** for remote access:
   ```bash
   sudo raspi-config
5. Update the system:
   ```bash
   sudo apt update && sudo apt upgrade -y

## **3️⃣ Installing Required Packages**
### **Install Dependencies**
1. Run the following command to install all necessary packages:
   pip install -r requirements.txt
2. This will install the following:
   1. Flask (Web Dashboard)
   2. MQTT (IoT Messaging)
   3. GPIO Control Libraries
   4. Camera Streaming Support

## **4️⃣ Wiring & Hardware Setup**
### **Connect Sensors, Motors, and Relays**
**Refer to assembly_instructions.txt for wiring diagrams**
1. Temperature Sensor (SHT4x) Wiring:
   - VCC → Pi 3.3V
   - GND → Pi GND
   - SDA/SCL → Pi I2C Pins (GPIO2 & GPIO3)
2. Egg Turner Motor Wiring:
   - Servo PWM Signal → Pi GPIO18
   - Stepper Dir & Step Pins → Pi GPIO22 & GPIO23
3. Relay Wiring for Heater/Humidifier
   - Heater Relay IN → Pi GPIO17
   - Humidifier Relay IN → Pi GPIO27

## **5️⃣ Running the Incubator System**
1. Start the main incubator script
   ```bash
   python3 src/incubator.py
2. Access the Web Dashboard
   - Once the system is running, access the dashboard via:
     - http://<raspberry-pi-ip>:5000
   - Here, you can monitor temperature, humidity, and egg turner status.
   - Click Refresh periodically to see updated sensor data.

## **6️⃣ Troubleshooting**
### **Common Issues & Fixes**
## Troubleshooting Guide

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| **Temperature not updating** | Sensor wiring issue | Check I2C connections & power |
| **Egg turner not moving** | Incorrect GPIO assignment | Verify pin configurations in `settings.json` |
| **No humidity control** | Relay module failure | Ensure relay switching via GPIO |
| **Web dashboard not loading** | Flask server not running | Restart with `python3 src/incubator.py` |

For more troubleshooting details, refer to docs/troubleshooting.md.

## **7️⃣ Next Steps**
✅ Fine-tune temperature and humidity targets in settings.json.
✅ Enable MQTT remote control for IoT monitoring.
✅ Implement logging and data visualization for long-term tracking.
✅ Develop advanced automation features for improved incubation efficiency.

📌 Your incubator system is now fully set up! 🚀🐣 If you have any additional refinements or questions, let me know, and I'll enhance this guide further as time permits! 🔧🐣