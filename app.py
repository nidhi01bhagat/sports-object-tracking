import gradio as gr
import cv2
import sys
import tempfile
import os
sys.path.insert(0, '.')
from src.detector import PersonDetector
from src.tracker import PlayerTracker
from src.annotator import FrameAnnotator

def track_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps   = cap.get(cv2.CAP_PROP_FPS) or 25
    w     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    out_path = tempfile.mktemp(suffix='.mp4')
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    detector  = PersonDetector(model_name='yolov8n.pt', confidence=0.35)
    tracker   = PlayerTracker()
    annotator = FrameAnnotator(trail_length=40)

    frame_idx = 0
    last_dets = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % 2 == 0:
            xyxy, conf, cls = detector.detect(frame)
            if len(xyxy) > 0:
                last_dets = tracker.update(xyxy, conf, cls)
            else:
                last_dets = None
        if last_dets is not None:
            frame = annotator.annotate(frame, last_dets)
        out.write(frame)
        frame_idx += 1

    cap.release()
    out.release()
    return out_path

demo = gr.Interface(
    fn=track_video,
    inputs=gr.Video(label="Upload Sports Video"),
    outputs=gr.Video(label="Tracked Output"),
    title="?? Sports Multi-Object Tracking",
    description="""
    ## YOLOv8 + ByteTrack Player Tracking
    Upload any sports video and get back an annotated video with:
    - Unique persistent IDs per player
    - Colored bounding boxes
    - Movement trajectory trails

    Built by Nidhi Bhagat | [GitHub](https://github.com/nidhi01bhagat/sports-object-tracking)
    """,
    examples=[],
    theme=gr.themes.Soft()
)

demo.launch()
