# Sports Multi-Object Tracking

> Real-time player detection and persistent ID tracking in cricket footage
> Built with YOLOv8 + ByteTrack + OpenCV

![Python](https://img.shields.io/badge/Python-3.11-blue)
![YOLOv8](https://img.shields.io/badge/Detector-YOLOv8n-purple)
![Tracker](https://img.shields.io/badge/Tracker-ByteTrack-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

## Video Source
Original video: https://www.youtube.com/shorts/Cdcmx576dtY

## Pipeline
Video Input ? Frame Extraction ? YOLOv8 Detection ? ByteTrack ? ID Assignment ? Annotated Output

## Setup

### Requirements
- Python 3.11
- 8GB RAM minimum

### Install dependencies
pip install -r requirements.txt

### Download video
py -3.11 -m yt_dlp https://www.youtube.com/shorts/Cdcmx576dtY -o input_video.mp4

### Run tracker
py -3.11 pipeline.py

## Project Structure
- src/detector.py  — YOLOv8 person detection
- src/tracker.py   — ByteTrack multi-object tracker
- src/annotator.py — Bounding boxes, ID labels, trail drawing
- pipeline.py      — Main runner script
- report/          — Technical report

## Tech Stack
- Detector : YOLOv8n (Ultralytics)
- Tracker  : ByteTrack (via Supervision)
- Annotation: OpenCV
- Language : Python 3.11

## Author
Nidhi Bhagat — github.com/nidhi01bhagat
