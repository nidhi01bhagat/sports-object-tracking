import cv2
import sys
sys.path.insert(0, r'C:\sports-tracker')
from src.detector import PersonDetector
from src.tracker import PlayerTracker
from src.annotator import FrameAnnotator

def run_pipeline(input_path, output_path, skip_frames=2):
    cap = cv2.VideoCapture(input_path)
    fps   = cap.get(cv2.CAP_PROP_FPS)
    w     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f'Video: {w}x{h} at {fps:.1f}fps | Total frames: {total}')

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps, (w, h)
    )

    detector  = PersonDetector(model_name='yolov8n.pt', confidence=0.35)
    tracker   = PlayerTracker()
    annotator = FrameAnnotator(trail_length=40)

    frame_idx = 0
    last_dets = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % skip_frames == 0:
            xyxy, conf, cls = detector.detect(frame)
            if len(xyxy) > 0:
                last_dets = tracker.update(xyxy, conf, cls)
            else:
                last_dets = None

        if last_dets is not None:
            frame = annotator.annotate(frame, last_dets)

        out.write(frame)
        frame_idx += 1
        print(f'\rProcessing frame {frame_idx}/{total}', end='', flush=True)

    cap.release()
    out.release()
    print(f'\n? Done! Output saved to: {output_path}')

if __name__ == '__main__':
    run_pipeline(
        input_path=r'C:\sports-tracker\input_video.mp4',
        output_path=r'C:\sports-tracker\outputs\tracked_output.mp4'
    )
