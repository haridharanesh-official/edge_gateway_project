
import json
import paho.mqtt.client as mqtt
from config.config import MQTT_BROKER, MQTT_PORT, CLIENT_ID, MQTT_TOPIC

client = mqtt.Client(client_id=CLIENT_ID)

def connect():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

def publish(data):
    try:
        payload = json.dumps(data)
        result = client.publish(MQTT_TOPIC, payload)
        return result.rc == 0
    except:
        return False
