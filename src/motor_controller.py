# 🐣 Egg Turner Motor Control - Adjusts turning schedule

import time
from gpiozero import Servo

TURNER_GPIO = 18
servo = Servo(TURNER_GPIO)

def turn_eggs():
    """Activates the egg turner motor on a scheduled interval."""
    angles = [-1, 0, 1]  # Left, Neutral, Right
    for angle in angles:
        servo.value = angle
        time.sleep(5)  # Adjust delay as needed
