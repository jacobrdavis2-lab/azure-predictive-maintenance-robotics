# iot_simulator.py
# Simulates telemetry from a robotic device for Jacob Davis's predictive maintenance pipeline
import time
import json
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Jacob Davis - IoT Hub device connection (development environment)
CONNECTION_STRING = "HostName=jacob-iot-hub.azure-devices.net;DeviceId=robot-jacob-001;SharedAccessKey=..."

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def generate_telemetry():
    """Generate realistic sensor data with occasional failure patterns."""
    return {
        "deviceId": "robot-jacob-001",
        "timestamp": time.time(),
        "vibration": round(random.gauss(0.5, 0.2), 2),
        "temperature": round(random.gauss(65, 5), 1),
        "current_draw": round(random.gauss(12, 2), 1),
        "run_hours": round(time.time() % 1000, 1),
        "error_log": "none" if random.random() > 0.05 else "motor_overload"
    }

while True:
    telemetry = generate_telemetry()
    # Simulate emerging failure signature for testing
    if random.random() < 0.02:
        telemetry["vibration"] = 2.5
        telemetry["temperature"] = 92.0
    message = Message(json.dumps(telemetry))
    client.send_message(message)
    print(f"Sent telemetry: {telemetry}")
    time.sleep(5)
