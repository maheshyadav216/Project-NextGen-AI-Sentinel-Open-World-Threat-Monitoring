#=============================================================================//
# Project/Tutorial       - NextGen AI Sentinel – Open-World Threat Monitoring
# Author                 - https://www.hackster.io/maheshyadav216
# Hardware               - NVIDIA JETSON ORIN NANO SUPER DEVELOPER KIT   
# Software               - Python, OpenCV, NanoOWL
# GitHub Repo of Project - https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring 
# Code last Modified on  - 16/05/2026
# Code/Content license   - (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
#============================================================================//
# Main Code

from nanoowl.owl_predictor import OwlPredictor
from PIL import Image
import cv2
import numpy as np
import asyncio
from telegram import Bot
from datetime import datetime
import paho.mqtt.publish as publish

BOT_TOKEN = "XXXX:XXXX"
CHAT_ID = "XXXXX"

# =========================
# MQTT Configuration
# =========================

MQTT_BROKER = "localhost"
MQTT_TOPIC = "emergency/alert"

async def send_telegram_alert(image_path):

    bot = Bot(token=BOT_TOKEN)

    # Send text message
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚨 THREAT CONFIRMED!\nWeapon detected by AI Sentinel."
    )

    # Send image
    with open(image_path, "rb") as photo:

        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=photo
        )

# Initialize NanoOWL
predictor = OwlPredictor()

# Detection prompts
texts = ["person", "rifle", "gun", "weapon"]

# Encode prompts once
text_encodings = predictor.encode_text(texts)

# Open video
cap = cv2.VideoCapture("videos/test.mp4")

threat_counter = 0
alert_sent = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize for better speed
    frame = cv2.resize(frame, (640, 480))

    # Convert OpenCV -> PIL
    image = Image.fromarray(
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ).convert("RGB")

    # Run detection
    predictions = predictor.predict(
        image=image,
        text=texts,
        text_encodings=text_encodings,
        threshold=0.12
    )

    boxes = predictions.boxes
    labels = predictions.labels
    scores = predictions.scores

    # Draw detections
    for box, label, score in zip(boxes, labels, scores):
        detected_object = texts[label]

        if detected_object in ["rifle", "gun", "weapon"]:
        	threat_counter +=  1
        x1, y1, x2, y2 = map(int, box)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0,255,0),
            2
        )

        text = f"{texts[label]} : {score:.2f}"

        cv2.putText(
            frame,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )
       
        cv2.putText(
            frame,
            f"Threat Counter : {threat_counter}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )
        if threat_counter >= 20:

            cv2.putText(
                frame,
                "THREAT CONFIRMED!",
                (20,90),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0,0,255),
                4
            )
            if not alert_sent:

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_path = f"alerts/alert_{timestamp}.jpg"
                cv2.imwrite(image_path, frame)
                asyncio.run(send_telegram_alert(image_path))
                alert_sent = True
               
                publish.single(
                MQTT_TOPIC,
                "THREAT",
                hostname=MQTT_BROKER
                )

    # Show frame
    cv2.imshow("AI Sentinel", frame)

    # ESC key to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
#============================================================================//