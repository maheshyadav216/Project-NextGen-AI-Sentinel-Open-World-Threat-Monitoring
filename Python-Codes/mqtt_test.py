#=============================================================================//
# Project/Tutorial       - NextGen AI Sentinel – Open-World Threat Monitoring
# Author                 - https://www.hackster.io/maheshyadav216
# Hardware               - NVIDIA JETSON ORIN NANO SUPER DEVELOPER KIT   
# Software               - Python, OpenCV, NanoOWL
# GitHub Repo of Project - https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring 
# Code last Modified on  - 16/05/2026
# Code/Content license   - (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
#============================================================================//
# MQTT Test
import paho.mqtt.publish as publish

BROKER = "localhost"
TOPIC = "emergency/alert"

publish.single(
    TOPIC,
    "THREAT",
    hostname=BROKER
)

print("THREAT message sent!")
#============================================================================//