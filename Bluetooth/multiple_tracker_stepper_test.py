import serial
import numpy as np
import threading
import time
import RPi.GPIO as GPIO
from pathlib import Path

GPIO.setmode(GPIO.BOARD)

# Set Stepper motor pins to 7, 11, 13, 15 (Depending on Board Number)
ControlPin = [7, 11, 13, 15]
# Set Stepper motor pins to 31, 33, 35, 37 (Depending on Board Number)
ControlPin2 = [31, 33, 35, 37]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
for pin in ControlPin2:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
# Set pins End.

# 4 Sequences
seq = [ [1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1] ]

b_device = Path("/dev/rfcomm0")

crd_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
crd_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
faceInfo = 0
cnt = 0
fin_x = 0
fin_y = 0
crd = [0, 0]
tmp = [0, 0]
tmp2 = [0, 0]

exception_flag = 0

def getFaceInfo():
    while(1):
        global exception_flag
        global faceInfo
        global crd
        global tmp
        global tmp2
        if(b_device.exists() == True):
            # Read Coordinates String via Bluetooth Communication
            try:
                ser = serial.Serial('/dev/rfcomm0')
                coord = ser.readline()
                coord = coord.decode('utf-8')
                coord = coord[0:-2]
            except serial.serialutil.SerialException:
                fin_x = 500
                fin_y = 1000
                print("Bluetooth connection lost")
                exception_flag = 1
                time.sleep(0.5)
                break
            else:
                pass
            crd = coord.split('/')
            tmp = crd[1].split(',')
            tmp2 = tmp[1].split(';')
            # crd[0] => crd_x tmp[0] => crd_y, tmp2[0] => face Id, tmp2[1] => number of faces

            faceInfo[int(tmp2[0])%10] = np.array([(int(float(crd[0])), int(float(tmp[0])), int(tmp2[0])%10)],
                        dtype=[('crd_x', (np.int32)), ('crd_y', np.int32), ('id', np.int32)])
            print(faceInfo)

def getCoord():
    while(True):
        global crd_x
        global crd_y
        global fin_x
        global fin_y
        global faceInfo
        global crd
        global tmp
        global tmp2

        if(tmp2[1] == '1'):
            crd_x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_x[0] = crd[0]
            crd_y[0] = tmp[0]
            print("Face ", end='')
            print(1)
            print("x = ", end='')
            print(crd_x[0])
            print("y = ", end='')
            print(crd_y[0])

        if(tmp2[1] == '2'):
            crd_x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(int(tmp2[0])%10 == 0):
                crd_x[0] = faceInfo[0]['crd_x']
                crd_y[0] = faceInfo[0]['crd_y']
                print("Face ", end='')
                print(1)
                print("x = ", end='')
                print(crd_x[0])
                print("y = ", end='')
                print(crd_y[0])
            elif(int(tmp2[0])%10 == 1):
                crd_x[1] = faceInfo[1]['crd_x']
                crd_y[1] = faceInfo[1]['crd_y']
                print("Face ", end='')
                print(2)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 2):
                crd_x[2] = faceInfo[2]['crd_x']
                crd_y[2] = faceInfo[2]['crd_y']
                print("Face ", end='')
                print(3)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 3):
                crd_x[3] = faceInfo[3]['crd_x']
                crd_y[3] = faceInfo[3]['crd_y']
                print("Face ", end='')
                print(4)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 4):
                crd_x[4] = faceInfo[4]['crd_x']
                crd_y[4] = faceInfo[4]['crd_y']
                print("Face ", end='')
                print(5)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 5):
                crd_x[5] = faceInfo[5]['crd_x']
                crd_y[5] = faceInfo[5]['crd_y']
                print("Face ", end='')
                print(6)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 6):
                crd_x[6] = faceInfo[6]['crd_x']
                crd_y[6] = faceInfo[6]['crd_y']
                print("Face ", end='')
                print(7)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 7):
                crd_x[7] = faceInfo[7]['crd_x']
                crd_y[7] = faceInfo[7]['crd_y']
                print("Face ", end='')
                print(8)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 8):
                crd_x[8] = faceInfo[8]['crd_x']
                crd_y[8] = faceInfo[8]['crd_y']
                print("Face ", end='')
                print(9)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 9):
                crd_x[9] = faceInfo[9]['crd_x']
                crd_y[9] = faceInfo[9]['crd_y']
                print("Face ", end='')
                print(10)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])

        if(tmp2[1] == '3'):
            crd_x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(int(tmp2[0])%10 == 0):
                crd_x[0] = faceInfo[0]['crd_x']
                crd_y[0] = faceInfo[0]['crd_y']
                print("Face ", end='')
                print(1)
                print("x = ", end='')
                print(crd_x[0])
                print("y = ", end='')
                print(crd_y[0])
            elif(int(tmp2[0])%10 == 1):
                crd_x[1] = faceInfo[1]['crd_x']
                crd_y[1] = faceInfo[1]['crd_y']
                print("Face ", end='')
                print(2)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 2):
                crd_x[2] = faceInfo[2]['crd_x']
                crd_y[2] = faceInfo[2]['crd_y']
                print("Face ", end='')
                print(3)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 3):
                crd_x[3] = faceInfo[3]['crd_x']
                crd_y[3] = faceInfo[3]['crd_y']
                print("Face ", end='')
                print(4)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 4):
                crd_x[4] = faceInfo[4]['crd_x']
                crd_y[4] = faceInfo[4]['crd_y']
                print("Face ", end='')
                print(5)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 5):
                crd_x[5] = faceInfo[5]['crd_x']
                crd_y[5] = faceInfo[5]['crd_y']
                print("Face ", end='')
                print(6)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 6):
                crd_x[6] = faceInfo[6]['crd_x']
                crd_y[6] = faceInfo[6]['crd_y']
                print("Face ", end='')
                print(7)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 7):
                crd_x[7] = faceInfo[7]['crd_x']
                crd_y[7] = faceInfo[7]['crd_y']
                print("Face ", end='')
                print(8)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 8):
                crd_x[8] = faceInfo[8]['crd_x']
                crd_y[8] = faceInfo[8]['crd_y']
                print("Face ", end='')
                print(9)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 9):
                crd_x[9] = faceInfo[9]['crd_x']
                crd_y[9] = faceInfo[9]['crd_y']
                print("Face ", end='')
                print(10)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])

        if(tmp2[1] == '4'):
            crd_x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(int(tmp2[0])%10 == 0):
                crd_x[0] = faceInfo[0]['crd_x']
                crd_y[0] = faceInfo[0]['crd_y']
                print("Face ", end='')
                print(1)
                print("x = ", end='')
                print(crd_x[0])
                print("y = ", end='')
                print(crd_y[0])
            elif(int(tmp2[0])%10 == 1):
                crd_x[1] = faceInfo[1]['crd_x']
                crd_y[1] = faceInfo[1]['crd_y']
                print("Face ", end='')
                print(2)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 2):
                crd_x[2] = faceInfo[2]['crd_x']
                crd_y[2] = faceInfo[2]['crd_y']
                print("Face ", end='')
                print(3)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 3):
                crd_x[3] = faceInfo[3]['crd_x']
                crd_y[3] = faceInfo[3]['crd_y']
                print("Face ", end='')
                print(4)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 4):
                crd_x[4] = faceInfo[4]['crd_x']
                crd_y[4] = faceInfo[4]['crd_y']
                print("Face ", end='')
                print(5)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 5):
                crd_x[5] = faceInfo[5]['crd_x']
                crd_y[5] = faceInfo[5]['crd_y']
                print("Face ", end='')
                print(6)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 6):
                crd_x[6] = faceInfo[6]['crd_x']
                crd_y[6] = faceInfo[6]['crd_y']
                print("Face ", end='')
                print(7)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 7):
                crd_x[7] = faceInfo[7]['crd_x']
                crd_y[7] = faceInfo[7]['crd_y']
                print("Face ", end='')
                print(8)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 8):
                crd_x[8] = faceInfo[8]['crd_x']
                crd_y[8] = faceInfo[8]['crd_y']
                print("Face ", end='')
                print(9)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 9):
                crd_x[9] = faceInfo[9]['crd_x']
                crd_y[9] = faceInfo[9]['crd_y']
                print("Face ", end='')
                print(10)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])

        if(tmp2[1] == '5'):
            crd_x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            crd_y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if(int(tmp2[0])%10 == 0):
                crd_x[0] = faceInfo[0]['crd_x']
                crd_y[0] = faceInfo[0]['crd_y']
                print("Face ", end='')
                print(1)
                print("x = ", end='')
                print(crd_x[0])
                print("y = ", end='')
                print(crd_y[0])
            elif(int(tmp2[0])%10 == 1):
                crd_x[1] = faceInfo[1]['crd_x']
                crd_y[1] = faceInfo[1]['crd_y']
                print("Face ", end='')
                print(2)
                print("x = ", end='')
                print(crd_x[1])
                print("y = ", end='')
                print(crd_y[1])
            elif(int(tmp2[0])%10 == 2):
                crd_x[2] = faceInfo[2]['crd_x']
                crd_y[2] = faceInfo[2]['crd_y']
                print("Face ", end='')
                print(3)
                print("x = ", end='')
                print(crd_x[2])
                print("y = ", end='')
                print(crd_y[2])
            elif(int(tmp2[0])%10 == 3):
                crd_x[3] = faceInfo[3]['crd_x']
                crd_y[3] = faceInfo[3]['crd_y']
                print("Face ", end='')
                print(4)
                print("x = ", end='')
                print(crd_x[3])
                print("y = ", end='')
                print(crd_y[3])
            elif(int(tmp2[0])%10 == 4):
                crd_x[4] = faceInfo[4]['crd_x']
                crd_y[4] = faceInfo[4]['crd_y']
                print("Face ", end='')
                print(5)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])
            elif(int(tmp2[0])%10 == 5):
                crd_x[5] = faceInfo[5]['crd_x']
                crd_y[5] = faceInfo[5]['crd_y']
                print("Face ", end='')
                print(6)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])
            elif(int(tmp2[0])%10 == 6):
                crd_x[6] = faceInfo[6]['crd_x']
                crd_y[6] = faceInfo[6]['crd_y']
                print("Face ", end='')
                print(7)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])
            elif(int(tmp2[0])%10 == 7):
                crd_x[7] = faceInfo[7]['crd_x']
                crd_y[7] = faceInfo[7]['crd_y']
                print("Face ", end='')
                print(8)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])
            elif(int(tmp2[0])%10 == 8):
                crd_x[8] = faceInfo[8]['crd_x']
                crd_y[8] = faceInfo[8]['crd_y']
                print("Face ", end='')
                print(9)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])
            elif(int(tmp2[0])%10 == 9):
                crd_x[9] = faceInfo[9]['crd_x']
                crd_y[9] = faceInfo[9]['crd_y']
                print("Face ", end='')
                print(10)
                print("x = ", end='')
                print(crd_x[4])
                print("y = ", end='')
                print(crd_y[4])

# Set defined functions to Thread
def getFaceInfo_thread():
    thread=threading.Thread(target=getFaceInfo)
    thread.daemon=True
    thread.start()

# Main
while True:
    if (b_device.exists() == True):
        getFaceInfo()
    else:
        print("Bluetooth not connected")
        time.sleep(5)
