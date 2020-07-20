import serial
import threading
import time
import re
import RPi.GPIO as GPIO
from pathlib import Path

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# You can connect servos to I/O pins including 7, 11, 12, 13, 15, 16, 18 & 22
# Set pin 22 as an output, and set servo_x as pin 22 as PWM
GPIO.setup(22,GPIO.OUT)
# Set pin 11 as an output, and set servo_y as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo_x = GPIO.PWM(22,100) # Note 22 is pin, 100 = 100Hz pulse
servo_y = GPIO.PWM(11,100) # Note 22 is pin, 100 = 100Hz pulse

servo_x.start(0)
servo_y.start(0)
time.sleep(1)

b_device = Path("/dev/rfcomm0")

crd_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
crd_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
faceInfo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cnt = 0
fin_x = 0
fin_y = 0
crd = [0, 0]
tmp = [0, 0]
tmp2 = [0, 0]
exception_flag = 0
faceId = 0
coord = 0
faceNum = 0
duty = 14

def readSerialLine():
    while(1):
        global exception_flag
        global fin_x
        global fin_y
        global coord
        global faceNum
        if(b_device.exists() == True):
            # Read Coordinates String via Bluetooth Communication
            try:
                ser = serial.Serial('/dev/rfcomm0')
                coord = ser.readline()
                coord = coord.decode('utf-8')
                coord = coord[0:-2]
                faceNum = coord.split(':')
                # faceNum[0] => crd infos, faceNum[1] => number of faces
            except serial.serialutil.SerialException:
                fin_x = 500
                fin_y = 1000
                print("Bluetooth connection lost")
                exception_flag = 1
                time.sleep(0.5)
                break
        else:
            continue

        fn = int(faceNum[1])
        # crd#[0] => crd_x, crd#[1] => crd_y
        if(fn == 1):
            fi1 = faceNum[0][0:-1]
            crd1 = fi1.split('/')
            print("faces = 1")
            print(crd1)
            fin_x = float(crd1[0])
            fin_y = float(crd1[1])
        elif(fn == 2):
            fi2 = re.split('!', faceNum[0][0:-1])
            crd1 = fi2[0].split('/')
            crd2 = fi2[1].split('/')
            print("faces = 2")
            print(crd1)
            print(crd2)
            fin_x = (float(crd1[0]) + float(crd2[0]))/2
            fin_y = (float(crd1[1]) + float(crd2[1]))/2
        elif(fn == 3):
            fi3 = re.split('!|"', faceNum[0][0:-1])
            crd1 = fi3[0].split('/')
            crd2 = fi3[1].split('/')
            crd3 = fi3[2].split('/')
            print("faces = 3")
            print(crd1)
            print(crd2)
            print(crd3)
            fin_x = (float(crd1[0]) + float(crd2[0]) + float(crd3[0]))/3
            fin_y = (float(crd1[1]) + float(crd2[1]) + float(crd3[1]))/3
        elif(fn == 4):
            fi4 = re.split('!|"|#', faceNum[0][0:-1])
            crd1 = fi4[0].split('/')
            crd2 = fi4[1].split('/')
            crd3 = fi4[2].split('/')
            crd4 = fi4[3].split('/')
            print("faces = 4")
            print(crd1)
            print(crd2)
            print(crd3)
            print(crd4)
            fin_x = (float(crd1[0]) + float(crd2[0]) + float(crd3[0]) + float(crd4[0]))/4
            fin_y = (float(crd1[1]) + float(crd2[1]) + float(crd3[1]) + float(crd4[1]))/4
        elif(fn == 5):
            fi5 = re.split('!|"|#|$', faceNum[0][0:-1])
            crd1 = fi5[0].split('/')
            crd2 = fi5[1].split('/')
            crd3 = fi5[2].split('/')
            crd4 = fi5[3].split('/')
            crd5 = fi5[4].split('/')
            print("faces = 5")
            print(crd1)
            print(crd2)
            print(crd3)
            print(crd4)
            print(crd5)
            fin_x = (float(crd1[0]) + float(crd2[0]) + float(crd3[0]) + float(crd4[0]) + float(crd5[0]))/5
            fin_y = (float(crd1[1]) + float(crd2[1]) + float(crd3[1]) + float(crd4[1]) + float(crd5[1]))/5
        else:
            fin_x = 500
            fin_y = 1000
        print("fin_x = ", end='')
        print(fin_x, end='')
        print(", fin_y = ", end='')
        print(fin_y)

def runServo_x():
    while True:
        global servo_x
        global fin_x
        #global fin_y
        global exception_flag
        global duty

        manx_rspeed = (fin_x - 600)/600
        manx_lspeed = (fin_x - 400)/600

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            fin_x = 500
            fin_y = 1000
            servo_x.ChangeDutyCycle(14)
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_x > 600):
            servo_x.ChangeDutyCycle(duty)
            time.sleep(0.1)
            duty = 14 + manx_rspeed
            # Run Servo Motor to Left
        elif(fin_x < 400):
            servo_x.ChangeDutyCycle(duty)
            time.sleep(0.1)
            duty = 14 + manx_lspeed
        else:
            duty = 14
            servo_x.ChangeDutyCycle(duty)
            time.sleep(0.1)

def runServo_y():
    while True:
        global servo_y
        #global fin_x
        global fin_y
        global exception_flag
        global duty

        manx_rspeed = (fin_y - 1100)/1200
        manx_lspeed = (fin_y - 900)/1200

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            servo_y.ChangeDutyCycle(14)
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_y > 1100):
            servo_y.ChangeDutyCycle(duty)
            time.sleep(0.1)
            duty = 14 + manx_rspeed
            # Run Servo Motor to Left
        elif(fin_y < 900):
            servo_y.ChangeDutyCycle(duty)
            time.sleep(0.1)
            duty = 14 + manx_lspeed
        else:
            duty = 14
            servo_y.ChangeDutyCycle(duty)
            time.sleep(0.1)

def readSerialLine_thread():
    thread = threading.Thread(target = readSerialLine)
    thread.daemon = True
    thread.start()

def runServo_y_thread():
    thread = threading.Thread(target = runServo_y)
    thread.daemon = True
    thread.start()

while(1):
    if(b_device.exists() == True):
        readSerialLine_thread()
        runServo_y_thread()
        runServo_x()
    else:
        print("Bluetooth not connected")
        time.sleep(5)
