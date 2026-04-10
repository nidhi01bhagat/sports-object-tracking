from ultralytics import YOLO
import numpy as np

class PersonDetector:
    def __init__(self, model_name='yolov8n.pt', confidence=0.35):
        self.model = YOLO(model_name)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]
        boxes = results.boxes
        if len(boxes) == 0:
            return np.zeros((0,4)), np.zeros((0,)), np.zeros((0,))
        mask = boxes.cls == 0
        xyxy = boxes.xyxy[mask].cpu().numpy()
        conf = boxes.conf[mask].cpu().numpy()
        cls  = boxes.cls[mask].cpu().numpy()
        return xyxy, conf, cls
