import cv2
import mediapipe as mp
from cvzone.SerialModule import SerialObject
import cvzone

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  arduino = SerialObject()
  previous_result = False
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
    

    face_appeared = results.detections and not previous_result
    face_disappeared = not results.detections and previous_result
    if face_appeared:
      print("Face-Appeared Passed")
      arduino.sendData([1])
    elif face_disappeared:
      print("Face-Disappeared Passed")
      arduino.sendData([0])

    if results.detections:
      previous_result = True
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    else:
      previous_result = False


    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
    if cv2.waitKey(5) & 0xFF == ord('2'):
      arduino.sendData([1])
    if cv2.waitKey(5) & 0xFF == ord('1'):
      arduino.sendData([0])
cap.release()