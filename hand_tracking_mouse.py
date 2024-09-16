import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import mouse
# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Initialize the previous positions
prev_x, prev_y = 0, 0

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a later selfie-view display
    img = cv2.flip(img, 1)

    # Convert the image color to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the landmark coordinates for the index finger tip and middle finger tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Convert normalized coordinates to pixel coordinates
            h, w, c = img.shape
            index_x, index_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            middle_x, middle_y = int(middle_finger_tip.x * w), int(middle_finger_tip.y * h)

            # Calculate the distance between the index and middle finger tips
            distance = np.linalg.norm(np.array([index_x, index_y]) - np.array([middle_x, middle_y]))

            # If the distance is below a certain threshold, simulate a mouse click
            if distance < 20:  # Adjust threshold as needed
                # pyautogui.middleClick()
                # pyautogui.hold
                mouse.press(button='middle')
                # time.sleep(0.1)
            # mouse.release(button='middle')
            # Calculate the screen coordinates for cursor movement
            screen_x = np.interp(index_x, (0, w), (0, screen_width))
            screen_y = np.interp(index_y, (0, h), (0, screen_height))

            # Smooth the cursor movement
            cur_x = prev_x + (screen_x - prev_x) / 5
            cur_y = prev_y + (screen_y - prev_y) / 5

            # Move the cursor
            pyautogui.moveTo(cur_x, cur_y)

            # Update the previous positions
            prev_x, prev_y = cur_x, cur_y

    # Display the image
    cv2.imshow('Hand Tracking', img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
