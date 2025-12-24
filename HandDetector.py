import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

model_path = 'hand_landmarker.task'

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
    running_mode=vision.RunningMode.VIDEO
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
p_time = 0

print("Hand detector started. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame from camera.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    frame_timestamp_ms = int(time.time() * 1000)

    detection_result = detector.detect_for_video(mp_image, frame_timestamp_ms)
    has_hand = len(detection_result.hand_landmarks) > 0

    c_time = time.time()
    fps = int(1 / (c_time - p_time)) if (c_time - p_time) > 0 else 0
    p_time = c_time

    cv2.rectangle(frame, (5, 5), (400, 80), (0, 0, 0), -1)

    hand_status = "HAND: DETECTED" if has_hand else "HAND: NOT FOUND"
    status_color = (0, 255, 0) if has_hand else (0, 0, 255)
    cv2.putText(frame, hand_status, (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

    cv2.putText(frame, f"FPS: {fps}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Hand Detector (MediaPipe Tasks)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting as requested by user.")
        break

cap.release()
detector.close()
cv2.destroyAllWindows()