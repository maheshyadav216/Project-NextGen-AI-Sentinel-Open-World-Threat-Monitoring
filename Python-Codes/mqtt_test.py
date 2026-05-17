import paho.mqtt.publish as publish

BROKER = "localhost"
TOPIC = "emergency/alert"

publish.single(
    TOPIC,
    "THREAT",
    hostname=BROKER
)

print("THREAT message sent!")
