---
title: Sports Object Tracking
emoji: F
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
python_version: "3.11"
app_file: app.py
pinned: false
---

# Sports Multi-Object Tracking

![Python](https://img.shields.io/badge/Python-3.11-blue)
![YOLOv8](https://img.shields.io/badge/Detector-YOLOv8n-purple)
![Tracker](https://img.shields.io/badge/Tracker-ByteTrack-green)
![HuggingFace](https://img.shields.io/badge/Demo-HuggingFace-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> Real-time player detection and persistent ID tracking in cricket footage
> Built with YOLOv8 + ByteTrack + OpenCV + Gradio

## Live Demo
Try the live demo on Hugging Face Spaces:
**https://huggingface.co/spaces/nidhi01bhagat/sports-object-tracking**

## Video Source
Original video: https://www.youtube.com/shorts/Cdcmx576dtY

## Pipeline
Video Input → Frame Extraction → YOLOv8 Detection → ByteTrack → ID Assignment → Annotated Output

## Results
![Screenshot 1](assets/screenshot_1.jpg)
![Screenshot 2](assets/screenshot_2.jpg)

## Setup
### Install
pip install -r requirements.txt

### Download video
py -3.11 -m yt_dlp https://www.youtube.com/shorts/Cdcmx576dtY -o input_video.mp4

### Run locally
py -3.11 pipeline.py

### Run Gradio app locally
py -3.11 app.py

## Project Structure
- src/detector.py   - YOLOv8 person detection
- src/tracker.py    - ByteTrack multi-object tracker
- src/annotator.py  - Bounding boxes, ID labels, trails
- pipeline.py       - Main runner script
- app.py            - Gradio web app (deployed on Hugging Face)
- report/           - Technical report

## Tech Stack
- Detector  : YOLOv8n (Ultralytics)
- Tracker   : ByteTrack (Supervision)
- Annotation: OpenCV
- Web App   : Gradio (Hugging Face Spaces)
- Language  : Python 3.11

## Author
Nidhi Bhagat
github.com/nidhi01bhagat
huggingface.co/spaces/nidhi01bhagat/sports-object-tracking
