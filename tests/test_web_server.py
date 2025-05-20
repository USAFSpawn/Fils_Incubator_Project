# 🐣 Web Server Testing - Verifies API functionality

import requests

BASE_URL = "http://localhost:5000"

def test_sensors_api():
    response = requests.get(f"{BASE_URL}/api/sensors")
    assert response.status_code == 200
    assert "temperature" in response.json()

def test_update_settings():
    new_settings = {
        "ALERTS": {
            "TEMP_HIGH_THRESHOLD_FAHRENHEIT": 100.0
        }
    }
    response = requests.post(f"{BASE_URL}/api/update-settings", json=new_settings)
    assert response.status_code == 200

test_sensors_api()
test_update_settings()
print("✅ Web server API tests passed!")
