# 🐣 Incubator Project - Motor Testing Script (test_motors.py)
# ✅ Verifies egg-turner motor functionality.

import time
from gpiozero import Servo

# Define GPIO assignment for egg-turner servo
GPIO_TURNER_SERVO = 18
servo = Servo(GPIO_TURNER_SERVO)

def test_motor_rotation():
    """Tests servo motor rotation between configurable angles."""
    angles = [-0.5, 0, 0.5]
    for angle in angles:
        print(f"🔄 Moving servo to position: {angle}")
        servo.value = angle
        time.sleep(2)

if __name__ == "__main__":
    print("⚙️ Running Motor Test...")
    test_motor_rotation()
