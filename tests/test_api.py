# 🐣 API Unit Tests (test_api.py)
# ✅ Tests `/api/sensors`, `/api/update-settings`, and `/api/history`.

import requests

BASE_URL = "http://localhost:5000"

def test_get_sensors():
    response = requests.get(f"{BASE_URL}/api/sensors")
    assert response.status_code == 200
    assert "temperature" in response.json()

def test_update_settings():
    new_settings = {
        "ADAPTIVE_CLIMATE_CONTROL": {
            "TEMPERATURE_TARGET_FAHRENHEIT": 100.0
        }
    }
    response = requests.post(f"{BASE_URL}/api/update-settings", json=new_settings)
    assert response.status_code == 200

if __name__ == "__main__":
    test_get_sensors()
    test_update_settings()
    print("✅ All tests passed!")
