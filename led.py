from cvzone.SerialModule import SerialObject
import cvzone
from time import sleep
import cv2
import serial.tools.list_ports
import os

# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p.description)

# PATH = os.path.abspath(cvzone.__file__)
# print(PATH)

arduino = SerialObject() #An automatic port is selected if no argument is selected


while True:
    arduino.sendData([1])
    sleep(3)
    arduino.sendData([0])
    sleep(1)
