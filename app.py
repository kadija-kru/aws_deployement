from flask import Flask, jsonify, request
import cv2
import torch
import torchvision
app = Flask(__name__)


# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/your/best.pt')

# Start capturing frames from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Perform object detection on the frame using YOLOv5
    results = model(frame)
if __name__ == '__main__':
    app.run()
