import gradio as gr
import cv2
import sys
import tempfile
sys.path.insert(0, '/app')
from src.detector import PersonDetector
from src.tracker import PlayerTracker
from src.annotator import FrameAnnotator

def track_video(video_path):
    if video_path is None:
        return None
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out_path = tempfile.mktemp(suffix=".mp4")
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    detector = PersonDetector(model_name="yolov8n.pt", confidence=0.35)
    tracker = PlayerTracker()
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

with gr.Blocks(title="Sports Tracking") as demo:
    gr.Markdown("# Sports Multi-Object Tracking")
    gr.Markdown("Upload a cricket or football video to get player IDs using YOLOv8 + ByteTrack.")
    with gr.Row():
        input_video = gr.Video(label="Upload Sports Video")
        output_video = gr.Video(label="Tracked Output")
    btn = gr.Button("Track Players")
    btn.click(fn=track_video, inputs=input_video, outputs=output_video)

demo.launch(server_name="0.0.0.0", server_port=7860)
