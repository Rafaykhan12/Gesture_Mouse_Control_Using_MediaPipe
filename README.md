# Gesture_Mouse_Control_Using_MediaPipe
Control your mouse cursor and clicks using hand gestures detected by a webcam

This project uses OpenCV, Mediapipe, and PyAutoGUI to control the mouse cursor and simulate mouse clicks based on hand gestures detected by a webcam. The system tracks hand landmarks, detects finger positions, and maps them to the screen for smooth cursor movement and click events.


## Use Case:
This project could be useful in situations where touch-based interaction is not practical, for example:

### Touch-Free Environments: 
In healthcare or industrial environments, touchless control can reduce the risk of contamination.
### Presentations: 
This system can be used for public presentations where a touchless way to control a computer is needed.
### In Giving Lectures:
This system provides a touchless way to control a computer. For example, while explaining software like SolidWorks, where mouse use is crucial, you can demonstrate features without needing to physically use a mouse. This enables you to interact seamlessly with your screen while maintaining audience engagement.
### Interactive Art Installations: 
Artists and developers could use this technology to create interactive art displays that react to user gestures.
### Accessibility: 
People with physical disabilities who have difficulty using traditional input devices like a mouse or keyboard can benefit from this.

## How the Project Works:
### Real-Time Hand Tracking: 
Uses Mediapipe to detect hand landmarks with high accuracy.
### Mouse Control and Click Simulation:
This system allows you to control the mouse cursor based on the position of your index finger. Additionally, it recognizes a pinch gesture (determined by the distance between the index and middle fingers) to simulate a mouse click
![handtracking_github-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b4c604c6-4fd6-47ad-b826-ab68f685887b)
## Features
- Hand gesture-based mouse control using a webcam.
- Smooth mouse cursor movement.
- Simulates mouse clicks based on the distance between the index and middle finger.


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
