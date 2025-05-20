# 🐣 Fils_Incubator_Project

This is my attempt at creating a **from-scratch, modernized, fully customizable** chicken egg **cabinet incubator**, built with a **Raspberry Pi 4B as the core**. It features **temperature and humidity control**, an **automatic egg turner**, and the ability to expand with additional features later. The design is **inspired by the GQF 1502 Digital Sportsman incubators**, but aims to be **more customizable and scalable**.

**ANY URLs used below are simply for reference purposes. I am developing this myself and am getting zero kickbacks or anything like that from any of these URLs.**

**--- --- --- ---**
## **🛠 Hardware Components**
### **1️⃣ Mainboard**
The central controller managing automation, data logging, and web interface.
- **Raspberry Pi 4B (Recommended)** – [Vilros Basic Starter Kit for Raspberry Pi 4](https://www.amazon.com/Vilros-Raspberry-Basic-Transparent-Cooled/dp/B089ZZ8DTV)
- **Raspberry Pi Zero 2 W (Alternative)** – [Vilros Raspberry Pi Zero 2 W Basic Starter Kit](https://www.amazon.com/Vilros-Raspberry-Aluminum-Multi-Purpose-Incudes/dp/B0CLPHV6S4)

### **2️⃣ Temperature & Humidity Sensors**
Monitors environmental conditions to maintain optimal incubation settings.
- **SHT45 (Latest Sensirion Sensor)** – [SHT45 Digital Sensor (Mouser)](https://www.mouser.com/new/sensirion/sensirion-sht4x-digital-sensor)
- **DHT22 (Alternative)** – [DHT22 Temperature/Humidity Sensor](https://www.amazon.com/dp/B08HR6ZTQK)

### **3️⃣ Heating & Humidity Control**
Provides warmth and humidity regulation for proper egg development.
- **PTC Heating Pad (12V)** – [PTC Heating Pad](https://www.aliexpress.com/item/32964774923.html)
- **Ultrasonic Humidifier** – [Levoit LV600S Smart Hybrid Humidifier](https://www.nytimes.com/wirecutter/reviews/the-best-humidifier/)

### **4️⃣ Egg Turning System**
Automates periodic rotation to mimic natural egg incubation.

#### **Egg Turner Motor**
- Servo Motor (MG995) – [MG995 Servo Motor](https://www.amazon.com/dp/B07Q4ZXHPZ)
- Stepper Motor (NEMA 17) – [NEMA 17 Stepper Motor](https://www.amazon.com/dp/B074X3C4J3)

#### **Egg Turner Racks & Trays**
- Universal Chicken Egg Trays (6-pack) – [Incubator Warehouse](https://incubatorwarehouse.com/collections/egg-incubator-accessories-incubator-egg-turners)
- GQF Automatic Egg Turner (Chicken & Quail) – [Berry Hill](https://berryhill.ca/collections/incubator-auto-turners)
- DIY Modular Egg Setter Tray (Flexy35Y) – [Hatching Time](https://hatchingtime.com/collections/diy-incubation-equipment)
- Plastic Egg Trays for Cabinet Incubators – [Amazon](https://www.amazon.com/incubator-trays/s?k=incubator+trays)

#### **Egg Turner Mounting Hardware**
- Metal Brackets for Egg Turner Motor Mounting – [Amazon](https://www.amazon.com/dp/B08HR6ZTQK)
- Adjustable Egg Rack Rails – [Incubator Warehouse](https://incubatorwarehouse.com/collections/egg-incubator-accessories-diy-incubator-parts)
- Egg Turner Arm Linkage Kit – [Berry Hill](https://berryhill.ca/collections/incubator-auto-turners)

### **5️⃣ Air Circulation & Ventilation**
Distributes heat and humidity evenly inside the incubator.
- **Brushless 12V DC Fan (PWM Controlled)** – [GDSTIME 12V Brushless Fan](https://www.amazon.com/dp/B0B1V5L4WB)

### **6️⃣ Camera Monitoring System**
Provides live video feeds for checking incubation progress remotely.
- **Raspberry Pi Camera Module v2.1** – [Vilros Raspberry Pi Camera Module V2](https://vilros.com/products/products-raspberry-pi-camera-module-v2)
- **USB Webcam (MotionEyeOS Compatible)** – [Logitech C920 Webcam (Amazon)](https://www.amazon.com/dp/B006JH8T3S)

### **7️⃣ Display & Control Interface**
Enables easy manual adjustments and status monitoring.
- **7-inch Raspberry Pi Touchscreen** – [Vilros 7" Official Raspberry Pi Touchscreen](https://vilros.com/products/official-raspberry-pi-7-touchscreen-with-pi-4-compatible-case)
- **OLED Display (128x64 I2C-based)** – [SSD1306 OLED Display (Amazon)](https://www.amazon.com/dp/B07SPW8XG6)

### **8️⃣ Power Management**
Handles various voltage requirements safely.
- **5V 3A Power Supply for Raspberry Pi** – [Vilros 27W 5V/5A USB-C Power Supply](https://www.amazon.com/Vilros-Raspberry-Compatible-USB-C-Supply/dp/B0CVJ195NQ)
- **12V PSU or Buck Converter** – [DCP3601 Buck Converter](https://community.st.com/t5/developer-news/simple-efficient-flexible-1a-buck-converter-powers-low-voltage/ba-p/774562)

### **9️⃣ Relay & Control Circuitry**
Switching components for automation.
- **Solid-State Relay (SSR 12V)** – [SSR 12V Relay (DigiKey)](https://www.digikey.com/en/products/filter/solid-state-relays-ssr/183)
- **MOSFET Module (IRF520)** – [IRF520 MOSFET Module](https://protosupplies.com/product/irf520-n-ch-mosfet-module/)

### **🔟 Enclosure & Assembly**
A well-insulated housing to retain stable incubation conditions.
- **Wood, Acrylic, Melamine, or Polycarbonate Cabinet** – Custom-built frame for durability built to your custom sizing requirements.
- **Foam Insulation or Reflective Wrap** – Helps maintain heat stability.
- **NOTE: I will provide more detailed specs on my various enclosure builds as I finish them.**

---

**--- --- --- ---**
## **🛠 Hardware Assembly & Wiring Guide**
This provides **step-by-step instructions** for assembling, wiring, and configuring the **Raspberry Pi-based automated egg incubator**.

---

## **1️⃣ Preparing the Enclosure**
- Choose an **insulated cabinet** to maintain stable temperature and humidity.
- Ensure **proper ventilation** using **adjustable vents and 12V DC fans**.
- Install **camera mounts** to position Raspberry Pi cameras for **clear egg monitoring**.

---

## **2️⃣ Installing the Raspberry Pi**
- **Mount the Raspberry Pi securely** inside the incubator.
- Connect **microSD card** with **Raspberry Pi OS Lite** installed.
- Use a **5V/3A power adapter** for stable power supply.
- Enable **SSH or VNC** for remote access.

---

## **3️⃣ Connecting Temperature & Humidity Sensors**
### **SHT4x (Recommended) Wiring**
- **VCC** → Raspberry Pi **3.3V**
- **GND** → Raspberry Pi **GND**
- **SDA** → Raspberry Pi **GPIO2 (I2C Data)**
- **SCL** → Raspberry Pi **GPIO3 (I2C Clock)**

### **DHT22 (Alternative) Wiring**
- **VCC** → Raspberry Pi **5V**
- **GND** → Raspberry Pi **GND**
- **Data** → Raspberry Pi **GPIO4**

---

## **4️⃣ Installing Heating Elements**
### **PTC Heating Pad Wiring via Relay**
- **Relay Module IN** → Raspberry Pi **GPIO17**
- **Relay VCC & GND** → Raspberry Pi **5V & GND**
- **Relay NO Terminal** → **Heating Pad Positive**
- **Heating Pad Negative** → **Power Supply Ground**

---

## **5️⃣ Setting Up Humidity System**
- Mount **ultrasonic humidifier** in an enclosed humidity chamber.
- **Relay Wiring for Automated Control**
  - **Relay Module IN** → Raspberry Pi **GPIO27**
  - **Relay Output** → **Humidifier Power Control**

---

## **6️⃣ Egg Turner Assembly/Installation**
### **1️⃣ Preparing the Egg Trays & Racks**
- Choose **modular egg trays** based on the egg size (chicken, duck, quail).
- Secure trays into **adjustable rails or mounting brackets** for smooth rotation.
- Ensure **even spacing** between trays for uniform heat and humidity distribution.

---

### **2️⃣ Installing the Egg Turner Motor**
#### **Servo Motor (MG995) Installation**
- **Mount the servo motor** on a **fixed side panel** inside the incubator.
- **Connect the servo arm to the egg tray** using an adjustable linkage.
- **Wiring:**
  - **VCC** → Raspberry Pi **5V**
  - **GND** → Raspberry Pi **GND**
  - **PWM Signal** → Raspberry Pi **GPIO18**

#### **Stepper Motor (NEMA 17) Installation**
- Attach the **stepper motor** to a **frame-mounted axle** for smooth tray movement.
- Secure the **motor shaft** with a **bracket or rotating pulley system**.
- **Wiring with A4988 Stepper Driver:**
  - **Step Signal** → Raspberry Pi **GPIO22**
  - **Dir Signal** → Raspberry Pi **GPIO23**
  - **Power** → **12V Supply**

---

### **3️⃣ Installing Turner Arm Linkage**
- **Use a flexible rod or metal linkage** to connect the **motor to the egg racks**.
- **Adjust linkage length** to **achieve proper turning angles** (tilt between 30°-45°).
- **Secure connections** with **screws or adjustable clamps** for stability.

---

### **4️⃣ Automating Egg Turning Cycles**
#### **Setting Up Python Control Script**
- Install **GPIO control libraries**:
   ```bash
   pip install gpiozero RPi.GPIO

---

## **7️⃣ Setting Up Camera Monitoring**
- Install **Raspberry Pi Camera Module** for monitoring incubation progress.
- **Connect CSI Port:** Attach the camera to Pi’s **CSI interface**.
- **Install MotionEyeOS for live streaming**.

---

## **8️⃣ Air Circulation & Fan Wiring**
### **PWM Fan Wiring**
- **VCC (12V)** → **Dedicated 12V Power Supply**
- **GND** → **Ground**
- **PWM Control** → Raspberry Pi **GPIO14**

---

## **9️⃣ Final System Check & Software Setup**
1. **NOTE: More detailed information in Software section.**
2. Flash **Raspberry Pi OS Lite**, update packages, and install dependencies:
   ```bash
   sudo apt update && sudo apt install python3-pip
   pip install flask fastapi paho-mqtt smbus2 opencv-python gpiozero

---


**--- --- --- ---**
## **⚡ Software Stack**
- 🐍 **Python** (for automation & sensor control)
- 🌐 **Flask/FastAPI** (for web dashboard)
- 📡 **MQTT Protocol** (for sensor communication)
- 🎥 **MotionEyeOS** (for live camera feed)
- 📜 **SQLite/InfluxDB** (for data logging)

---

**--- --- --- ---**
## **⚡ Software Components**
The following software components form the backbone of the **incubator automation system**, enabling **sensor control, web monitoring, data logging, and remote access**.

### **1️⃣ Core Operating System**
Handles the core system functionality, boot process, and environment setup.
- **Raspberry Pi OS Lite (Recommended)** – Lightweight, headless Debian-based OS optimized for embedded applications.
- **Alternative:** Ubuntu Server for Raspberry Pi.
- **Official Site:** [Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/)
- **Installation Instructions:**
   - Download **Raspberry Pi Imager** and flash **Raspberry Pi OS Lite** onto a microSD card.
   - Insert the card, boot the Pi, and enable SSH/VNC for remote access.

---

### **2️⃣ Programming Language & Essential Libraries**
Serves as the **primary automation control framework**.
- **Python 3.x (Core Language)** – Used for handling sensor data, automation, and logic processing.
- **Libraries:**
  - `gpiozero` – Interface for controlling motors and relays.
  - `smbus2` – Communicates with I2C-based temperature/humidity sensors.
  - `paho-mqtt` – Enables real-time MQTT messaging for IoT connectivity.
  - `opencv-python` – Handles live camera feeds and image processing.
- **Installation Command:**
   ```bash
   sudo apt update && sudo apt install python3 python3-pip
   pip install gpiozero smbus2 paho-mqtt opencv-python

---
