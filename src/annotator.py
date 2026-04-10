import cv2
import numpy as np

def id_to_color(track_id):
    np.random.seed(int(track_id) * 42)
    return tuple(int(c) for c in np.random.randint(50, 230, 3))

class FrameAnnotator:
    def __init__(self, trail_length=30):
        self.trails = {}
        self.trail_length = trail_length

    def annotate(self, frame, detections):
        if detections.tracker_id is None:
            return frame
        for i in range(len(detections.xyxy)):
            x1, y1, x2, y2 = map(int, detections.xyxy[i])
            tid = int(detections.tracker_id[i])
            color = id_to_color(tid)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            label = f'ID {tid}'
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame, (x1, y1 - h - 8), (x1 + w + 4, y1), color, -1)
            cv2.putText(frame, label, (x1 + 2, y1 - 4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            self.trails.setdefault(tid, []).append((cx, cy))
            self.trails[tid] = self.trails[tid][-self.trail_length:]
            pts = self.trails[tid]
            for j in range(1, len(pts)):
                alpha = j / len(pts)
                c = tuple(int(v * alpha) for v in color)
                cv2.line(frame, pts[j-1], pts[j], c, 2)
        return frame
