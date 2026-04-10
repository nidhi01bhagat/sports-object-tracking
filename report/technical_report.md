# Technical Report — Multi-Object Detection and Tracking

## Project Overview
This project implements a real-time multi-object detection and tracking pipeline
applied to cricket sports footage using YOLOv8 and ByteTrack.

Video Source: https://www.youtube.com/shorts/Cdcmx576dtY
Video Resolution: 360x640 (portrait/vertical)
Total Frames: 72 at 6fps

## Model Used — YOLOv8n (Ultralytics)
- Pre-trained on COCO dataset (80 classes)
- Class 0 = Person (only class we track)
- Confidence threshold: 0.35
- Chosen for: speed, accuracy, ease of use on CPU
- Model size: ~6MB (nano version)

## Tracker Used — ByteTrack (via Supervision)
- Two-stage matching algorithm
- Stage 1: High confidence detections matched via IoU
- Stage 2: Low confidence detections matched to lost tracklets
- Maintains persistent IDs without needing a separate Re-ID model
- Handles brief occlusion by keeping tracklets alive for N frames

## Why YOLOv8 + ByteTrack?
- YOLOv8 is the fastest and most accurate real-time detector available
- ByteTrack is lightweight and works well without GPU
- Together they process cricket footage efficiently on 8GB RAM CPU
- Supervision library makes integration clean and modular

## How ID Consistency is Maintained
- Each detected person gets a unique integer ID from ByteTrack
- IoU-based Hungarian algorithm matches detections frame to frame
- Lost tracklets are kept alive for 30 frames before ID is retired
- Colors are seeded from track ID so same player always shows same color
- Trajectory trails show movement history of each tracked player

## Pipeline Architecture
Video Input
    ?
Frame Extraction (OpenCV, every 2 frames)
    ?
YOLOv8n Detection (person class only)
    ?
ByteTrack ID Assignment
    ?
Frame Annotation (boxes + IDs + trails)
    ?
Output Video (MP4)

## Results
- Successfully tracked players across 72 frames
- Persistent IDs maintained throughout the video
- Colored bounding boxes drawn per player
- Trajectory trails show movement paths
- Output video: outputs/tracked_output.mp4

## Challenges Faced
1. Low FPS (6fps) means fewer frames for tracker to work with
2. Portrait video (360x640) means players are small in frame
3. Fast motion causes brief detection drops between frames
4. Similar jersey colors make players look alike to the model

## Failure Cases Observed
1. When two players overlap, IDs can switch after separation
2. Players at edge of frame get partially detected
3. Fast bowling action causes motion blur reducing confidence

## Possible Improvements
1. Add Re-ID model (OSNet) for appearance-based matching
2. Use larger YOLOv8 model (yolov8m) for better accuracy
3. Run at native resolution instead of resized frames
4. Add team clustering using jersey color histograms
5. Add speed estimation using pixel displacement per frame
6. Add heatmap visualization of player movement zones

## Tech Stack
- Python 3.11
- YOLOv8n (Ultralytics 8.4.36)
- ByteTrack (Supervision 0.27.0)
- OpenCV 4.13.0
- NumPy 2.4.4
