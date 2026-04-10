# Technical Report — Multi-Object Detection and Tracking

## Project Overview
Real-time multi-object detection and tracking pipeline
applied to cricket sports footage using YOLOv8 and ByteTrack.

Video Source: https://www.youtube.com/shorts/Cdcmx576dtY
Video Resolution: 360x640 (portrait)
Total Frames: 72 at 6fps

## Model — YOLOv8n
- Pre-trained on COCO dataset
- Only tracking class 0 (person)
- Confidence threshold: 0.35
- Chosen for speed and accuracy on CPU

## Tracker — ByteTrack
- Two-stage IoU matching
- Maintains IDs without separate Re-ID model
- Handles brief occlusion by keeping tracklets alive

## Why This Combination
- YOLOv8 is fastest real-time detector available
- ByteTrack is lightweight, works well without GPU
- Together they work efficiently on 8GB RAM

## How ID Consistency Works
- Each person gets unique integer ID from ByteTrack
- IoU Hungarian algorithm matches detections frame to frame
- Lost tracklets kept alive for 30 frames before retiring
- Same ID always gets same color via seeded random color

## Results
- 72 frames processed successfully
- Persistent IDs maintained throughout video
- Colored bounding boxes per player
- Trajectory trails showing movement paths

## Challenges
- Low FPS (6fps) gives tracker less data to work with
- Portrait video means players appear small
- Fast motion causes brief detection drops
- Similar jerseys make players look alike to model

## Failure Cases
- Overlapping players can cause ID switches
- Edge of frame players get partial detections
- Fast bowling causes motion blur

## Possible Improvements
- Add Re-ID model for appearance matching
- Use yolov8m for better accuracy
- Add team clustering by jersey color
- Add speed estimation
- Add heatmap of player movement
