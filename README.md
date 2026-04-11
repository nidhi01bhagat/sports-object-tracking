---
title: Sports Object Tracking
emoji: ??
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.0"
python_version: "3.11"
app_file: app.py
pinned: false
---

# ?? Sports Multi-Object Tracking

> Real-time player detection and persistent ID tracking in cricket footage
> Built with YOLOv8 + ByteTrack + OpenCV

![Python](https://img.shields.io/badge/Python-3.11-blue)
![YOLOv8](https://img.shields.io/badge/Detector-YOLOv8n-purple)
![Tracker](https://img.shields.io/badge/Tracker-ByteTrack-green)

## Video Source
Original video: https://www.youtube.com/shorts/Cdcmx576dtY

## How to Use
1. Upload a sports video
2. Wait for processing
3. Download the annotated output video with player IDs

## Pipeline
Video Input ? YOLOv8 Detection ? ByteTrack ? ID Assignment ? Annotated Output

## Tech Stack
- YOLOv8n (Ultralytics)
- ByteTrack (Supervision)
- OpenCV
- Python 3.11

## Author
Nidhi Bhagat | github.com/nidhi01bhagat/sports-object-tracking
