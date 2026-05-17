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
