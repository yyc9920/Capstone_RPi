import serial
import threading
import time
import re
import RPi.GPIO as GPIO
import pigpio
from pathlib import Path

servo_x = pigpio.pi() # Note 22 is pin, 100 = 100Hz pulse
servo_y = pigpio.pi() # Note 22 is pin, 100 = 100Hz pulse

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
duty_x = 1475 # halt duty cycle
duty_y = 2000 # Perpendicular duty cycle

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
                fin_y = 500
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
            fi5 = re.split('!|"|#', faceNum[0][0:-1])
            fi_tmp = fi5[3].split('$')
            crd1 = fi5[0].split('/')
            crd2 = fi5[1].split('/')
            crd3 = fi5[2].split('/')
            crd4 = fi_tmp[0].split('/')
            crd5 = fi_tmp[1].split('/')
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
            fin_y = 500
        print("fin_x = ", end='')
        print(fin_x, end='')
        print(", fin_y = ", end='')
        print(fin_y)

def runServo_x():
    while True:
        global servo_x
        global fin_x
        global fin_y
        global exception_flag
        global duty_x
        global duty_y

        manx_rspeed = (fin_x - 600)/20
        manx_lspeed = (fin_x - 400)/20

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            fin_x = 500
            fin_y = 500
            duty_x = 1475
            duty_y = 2000
            servo_x.set_servo_pulsewidth(25, 1475)
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_x > 600):
            servo_x.set_servo_pulsewidth(25, duty_x)
            time.sleep(0.05)
            duty_x = 1475 + manx_rspeed
        # Run Servo Motor to Left
        elif(fin_x < 400):
            servo_x.set_servo_pulsewidth(25, duty_x)
            time.sleep(0.05)
            duty_x = 1475 + manx_lspeed
        else:
            servo_x.set_servo_pulsewidth(25, 1475)
            time.sleep(0.05)

def runServo_y():
    while True:
        global servo_y
        #global fin_x
        global fin_y
        global exception_flag
        global duty_y

        manx_rspeed = (fin_y - 600)/1500
        manx_lspeed = (fin_y - 400)/1500

        if(duty_y > 2500):
            duty_y = 2500
        if(duty_y < 1500):
            duty_y = 1500

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            duty_y = 2000
            servo_y.set_servo_pulsewidth(17, 2000)
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_y > 600):
            servo_y.set_servo_pulsewidth(17, duty_y)
            time.sleep(0.05)
            duty_y = duty_y - manx_rspeed
        # Run Servo Motor to Left
        elif(fin_y < 400):
            servo_y.set_servo_pulsewidth(17, duty_y)
            time.sleep(0.05)
            duty_y = duty_y - manx_lspeed
        else:
            time.sleep(0.05)

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
