# 🔧 Troubleshooting Guide

## **Common Issues & Fixes**
| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| No temperature update | Sensor wiring issue | Verify I2C connection |
| Egg turner not moving | Incorrect GPIO setup | Check motor config in `settings.json` |
| Web dashboard not loading | Flask server not running | Restart with `python3 src/web_server.py` |
