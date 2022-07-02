import cv2
import mediapipe as mp
# from cvzone.SerialModule import SerialObject
# import cvzone
# from time import sleep

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  # arduino = SerialObject()
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")

      continue
    
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.detection:
      for detection in results.detection:
        mp_drawing.draw_detection(image, detection)

    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))

    # face_appeared = results.detection and not previous_results.detection
    # face_disappeared = not results.detection and previous_results.detection
    # if face_appeared:
    #   arduino.sendData([1])
    # elif face_disappeared:
    #   arduino.sendData([0])

    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
    
cap.release()


