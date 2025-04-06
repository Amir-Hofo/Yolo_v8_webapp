# Yolo v8 App
[WebApp Link](https://yolov8-webapp.streamlit.app)  
A Streamlit-based web application for running various computer vision tasks using YOLO v8 models.

...

---
Run program with this command:

```bash
streamlit run main.py
```

---
![Screen Shot 1404-01-17 at 10 11 57 AM](https://github.com/user-attachments/assets/16aa972a-01de-4c0c-99a5-efe7d138ad22)

![Screen Shot 1404-01-17 at 10 11 39 AM](https://github.com/user-attachments/assets/d70f0404-7aeb-49ac-8cbd-037b1b70a696)

![Screen Shot 1404-01-17 at 10 07 52 AM](https://github.com/user-attachments/assets/d24e6262-cdf6-44da-8833-de238218735b)

---
## Features

- **Multiple Task Support:**
  - Object Detection
  - Segmentation
  - Video Tracking
  - Body Position Detection

- **Input Types:**
  - Images (jpg, jpeg, png)
  - Videos (mp4, mkv)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Amir-Hofo/Yolo_v8_app.git
cd Yolo_v8_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. A browser window will automatically open, displaying the application page.

3. Select your input type (image/video)
4. Choose the desired task
5. Upload your file
6. Wait for processing
7. Download the results

## Models

The application uses YOLOv8 models for different tasks:
- yolov8n.pt - Object Detection, Video Tracking
- yolov8n-seg.pt - Segmentation
- yolov8n-pose.pt - Body Position Detection
