import supervision as sv

class PlayerTracker:
    def __init__(self):
        self.tracker = sv.ByteTrack()

    def update(self, xyxy, confidences, class_ids):
        detections = sv.Detections(
            xyxy=xyxy,
            confidence=confidences,
            class_id=class_ids.astype(int)
        )
        return self.tracker.update_with_detections(detections)
