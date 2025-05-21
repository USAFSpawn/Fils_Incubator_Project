# 🐣 Stepper Motor Controller - Egg Turner System
# ✅ Controls NEMA 23 stepper motor for precise tray tilting.
# ✅ Configurable tilt angles (30-45°) over a set time.
# ✅ Returns to level position for tray removal.

import RPi.GPIO as GPIO
import time
import json

# Load settings from JSON
CONFIG_FILE = "../config/settings.json"

def load_settings():
    """Loads system configuration from settings.json."""
    with open(CONFIG_FILE, "r") as config_file:
        return json.load(config_file)

settings = load_settings()

# GPIO Pin Assignments
STEP_PIN = settings["STEPPER_MOTOR"]["STEP_PIN"]
DIR_PIN = settings["STEPPER_MOTOR"]["DIR_PIN"]
ENABLE_PIN = settings["STEPPER_MOTOR"]["ENABLE_PIN"]

# Tilt Configuration
TILT_ANGLE = settings["STEPPER_MOTOR"]["TILT_ANGLE_DEGREES"]  # 30-45°
TILT_DURATION = settings["STEPPER_MOTOR"]["TILT_DURATION_SECONDS"]  # XX seconds
TILT_INTERVAL = settings["STEPPER_MOTOR"]["TILT_INTERVAL_MINUTES"]  # XX minutes

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

def step_motor(steps, direction):
    """Moves stepper motor to precise angle."""
    GPIO.output(DIR_PIN, direction)
    GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable motor

    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.01)

    GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable motor

def tilt_trays():
    """Tilts trays to configured angle and returns to level."""
    steps_per_degree = settings["STEPPER_MOTOR"]["STEPS_PER_DEGREE"]
    tilt_steps = int(TILT_ANGLE * steps_per_degree)

    print(f"🔄 Tilting trays to {TILT_ANGLE}°...")
    step_motor(tilt_steps, GPIO.HIGH)
    time.sleep(TILT_DURATION)

    print("🔄 Returning trays to level...")
    step_motor(tilt_steps, GPIO.LOW)

# Run tilt cycle at configured intervals
while True:
    tilt_trays()
    time.sleep(TILT_INTERVAL * 60)  # Convert minutes to seconds
