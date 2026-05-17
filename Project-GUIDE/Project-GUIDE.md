# Next Gen AI Sentinel – Open-World Threat Monitoring using Vision Transformers on the Edge

## Overview

Next Gen AI Sentinel is an AI-powered real-time surveillance and threat response system built on the NVIDIA Jetson Orin Nano platform using Vision Transformer–based Open-Vocabulary Detection. Unlike traditional CCTV analytics systems that are restricted to fixed object classes, this project uses NanoOWL and Zero-Shot Learning to detect threats dynamically through natural language prompts such as "weapon," "rifle," "gun," or "masked person" without requiring custom dataset training for every new category.

The system processes CCTV video feeds locally on the edge device using CUDA-accelerated inference, enabling low-latency, privacy-focused real-time monitoring. To reduce false alarms, a custom multi-frame threat confirmation logic verifies detections across consecutive frames before triggering alerts.

Once a threat is confirmed, the AI Sentinel automatically captures evidence snapshots, sends instant Telegram alerts with images, and activates a physical IoT-based emergency response system using the Arduino Oplà IoT Kit over MQTT communication. The Oplà device acts as a local smart emergency console by turning all onboard RGB LEDs red, displaying warning messages on the OLED screen, and activating an audible buzzer alarm.

By combining Edge AI, Vision Transformers, Open-Vocabulary Detection, IoT communication, and embedded hardware response into a single integrated workflow, this project demonstrates a modern cyber-physical security system capable of intelligent real-time threat monitoring and response.

---

# Key Features

- Open-Vocabulary Threat Detection using NanoOWL
- Zero-Shot AI Detection using natural language prompts
- Real-Time CCTV Video Processing
- CUDA-Accelerated Inference on Jetson Orin Nano
- Multi-Frame Threat Verification Logic
- Telegram Alert System with Evidence Images
- MQTT-based IoT Communication
- Arduino Oplà IoT Emergency Alert Console
- OLED Warning Interface
- Pulsing RED Emergency LEDs
- Audible Alarm using Piezo Buzzer
- Fully Local Edge AI Processing

---

# System Architecture

```text
CCTV Video Feed
        ↓
Jetson Orin Nano
        ↓
NanoOWL Vision Transformer
(Open-Vocabulary Detection)
        ↓
Threat Verification Logic
(Multi-frame confirmation)
        ↓
THREAT CONFIRMED
        ↓
├── Telegram Alert
├── Screenshot Evidence
├── MQTT Alert Publish
└── Local Event Logging
        ↓
Arduino Oplà IoT Kit
├── Pulsing RED LEDs
├── OLED Warning Display
└── Audible Emergency Buzzer
```

---

# Hardware Used

## Edge AI System

- NVIDIA Jetson Orin Nano Super Developer Kit
- NVMe SSD Storage
- Ethernet / WiFi Network

## IoT Emergency Alert System

- Arduino Oplà IoT Kit
- Arduino MKR WiFi 1010
- MKR IoT Carrier
  - RGB LEDs
  - OLED Display
  - Piezo Buzzer

---

# Software & AI Stack

## AI & Computer Vision

- Python
- OpenCV
- PyTorch
- CUDA
- NanoOWL
- Vision Transformers (ViTs)
- Zero-Shot Learning

## IoT & Communication

- MQTT
- Mosquitto MQTT Broker
- Telegram Bot API
- Arduino IDE

---

# How It Works

1. CCTV video feed is processed frame-by-frame on the Jetson Orin Nano.
2. NanoOWL performs Open-Vocabulary Detection using natural language prompts such as:

```python
["person", "rifle", "gun", "weapon"]
```

3. The AI detects suspicious objects in real time.
4. A custom threat verification counter checks detections across multiple consecutive frames.
5. Once the threat threshold is crossed:
   - "THREAT CONFIRMED" state activates
   - Screenshot evidence is captured
   - Telegram alert is sent with image
   - MQTT message is published
6. Arduino Oplà IoT Kit receives the MQTT alert and:
   - Pulses RED LEDs
   - Displays warning message on OLED
   - Activates buzzer alarm

---

# Demo Workflow

```text
1. Start AI Sentinel
2. CCTV footage begins
3. AI detects weapon
4. Threat counter increases
5. THREAT CONFIRMED
6. Telegram alert arrives
7. Evidence image received
8. Oplà LEDs pulse RED
9. OLED warning screen activates
10. Emergency buzzer sounds
```

---

# Project Screenshots

## AI Detection System

Add screenshots here:

```text
/screenshots/ai_detection.png
/screenshots/threat_confirmed.png
/screenshots/telegram_alert.png
```

## Arduino Oplà Alert Console

Add photos here:

```text
/screenshots/opla_armed_mode.jpg
/screenshots/opla_threat_mode.jpg
```

---

# Future Improvements

- NanoSAM Integration for Instance Segmentation
- TensorRT Optimization
- Multi-Camera Support
- RTSP CCTV Integration
- REST API Prompt Updates
- Cloud Dashboard
- Threat Logging Database
- Face Recognition Module

---

# GitHub Topics

```text
jetson-orin-nano
edge-ai
computer-vision
vision-transformers
nanoowl
opencv
iot
mqtt
telegram-bot
zero-shot-learning
open-vocabulary-detection
```

---

# Author

Mahesh Yadav

Project: Next Gen AI Sentinel – Open-World Threat Monitoring using Vision Transformers on the Edge

