# Gesture_Mouse_Control_Using_MediaPipe
Control your mouse cursor and clicks using hand gestures detected by a webcam

This project uses OpenCV, Mediapipe, and PyAutoGUI to control the mouse cursor and simulate mouse clicks based on hand gestures detected by a webcam. The system tracks hand landmarks, detects finger positions, and maps them to the screen for smooth cursor movement and click events.

## Features
- Hand gesture-based mouse control using a webcam.
- Smooth mouse cursor movement.
- Simulates mouse clicks based on the distance between the index and middle finger.
![handtracking_github-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b4c604c6-4fd6-47ad-b826-ab68f685887b)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Rafaykhan12/Gesture_Mouse_Control_Using_MediaPipe.git
   cd Gesture_Mouse_Control_Using_MediaPipe
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Python script to start hand tracking and mouse control:
   ```bash
   python hand_tracking_mouse.py
### 2. `requirements.txt`
```txt
opencv-python
mediapipe
pyautogui
numpy
mouse
