#=============================================================================//
# Project/Tutorial       - NextGen AI Sentinel – Open-World Threat Monitoring
# Author                 - https://www.hackster.io/maheshyadav216
# Hardware               - NVIDIA JETSON ORIN NANO SUPER DEVELOPER KIT   
# Software               - Python, OpenCV, NanoOWL
# GitHub Repo of Project - https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring 
# Code last Modified on  - 16/05/2026
# Code/Content license   - (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
#============================================================================//
# Testing Images

from nanoowl.owl_predictor import OwlPredictor
from PIL import Image
import cv2
import numpy as np

# Load image
image_path = "images/test.png"
image = Image.open(image_path).convert("RGB")

# Initialize predictor
predictor = OwlPredictor()

# Text prompts
texts = ["person", "rifle", "gun", "weapon"]

# Encode text
text_encodings = predictor.encode_text(texts)

# Run prediction
predictions = predictor.predict(
    image=image,
    text=texts,
    text_encodings=text_encodings,
    threshold=0.1
)

# Convert image for OpenCV
frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Draw detections
boxes = predictions.boxes
labels = predictions.labels
scores = predictions.scores

for box, label, score in zip(boxes, labels, scores):

    x1, y1, x2, y2 = map(int, box)

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

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

# Show result
cv2.imshow("Detection", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
#============================================================================//