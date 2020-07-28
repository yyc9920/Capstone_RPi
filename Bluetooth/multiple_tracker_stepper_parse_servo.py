import serial
import threading
import time
import re
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
duty_y = 2100 # Perpendicular duty cycle
servo_y.set_servo_pulsewidth(17, 2100)
time.sleep(2)

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
                fin_y = 350
                print("Bluetooth connection lost")
                exception_flag = 1
                time.sleep(0.5)
                break
        else:
            fin_x = 500
            fin_y = 500
            continue

        fn = int(faceNum[1])
        # crd#[0] => crd_x, crd#[1] => crd_y
        if(fn == 1):
            fi1 = faceNum[0][0:-1]
            crd1 = fi1.split('/')
            print('\033[36m' + "faces = 1" + '\033[0m')
            print(crd1)
            fin_x = float(crd1[0])
            fin_y = float(crd1[1])
        elif(fn == 2):
            fi2 = re.split('!', faceNum[0][0:-1])
            crd1 = fi2[0].split('/')
            crd2 = fi2[1].split('/')
            print('\033[36m' + "faces = 2" + '\033[0m')
            print(crd1)
            print(crd2)
            fin_x = (float(crd1[0]) + float(crd2[0]))/2
            fin_y = (float(crd1[1]) + float(crd2[1]))/2
        elif(fn == 3):
            fi3 = re.split('!|"', faceNum[0][0:-1])
            crd1 = fi3[0].split('/')
            crd2 = fi3[1].split('/')
            crd3 = fi3[2].split('/')
            print('\033[36m' + "faces = 3" + '\033[0m')
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
            print('\033[36m' + "faces = 4" + '\033[0m')
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
            print('\033[36m' + "faces = 5" + '\033[0m')
            print(crd1)
            print(crd2)
            print(crd3)
            print(crd4)
            print(crd5)
            fin_x = (float(crd1[0]) + float(crd2[0]) + float(crd3[0]) + float(crd4[0]) + float(crd5[0]))/5
            fin_y = (float(crd1[1]) + float(crd2[1]) + float(crd3[1]) + float(crd4[1]) + float(crd5[1]))/5
        else:
            fin_x = 500
            fin_y = 350
        print('\033[91m' + 'fin_x = ', end='')
        print(fin_x, end='')
        print(', fin_y = ', end='')
        print(fin_y, end='')
        print('\033[0m')

def runServo_x():
    while True:
        global servo_x
        global fin_x
        global fin_y
        global exception_flag
        global duty_x
        global duty_y

        manx_rspeed = (fin_x - 550)/10
        manx_lspeed = (fin_x - 450)/10

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            duty_x = 1475
            servo_x.set_servo_pulsewidth(25, 1475)
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_x > 550):
            servo_x.set_servo_pulsewidth(25, duty_x)
            duty_x = 1475 + manx_rspeed
            time.sleep(0.03)
        # Run Servo Motor to Left
        elif(fin_x < 450):
            servo_x.set_servo_pulsewidth(25, duty_x)
            duty_x = 1475 + manx_lspeed
            time.sleep(0.03)
        else:
            servo_x.set_servo_pulsewidth(25, 1475)

def runServo_y():
    while True:
        global servo_y
        #global fin_x
        global fin_y
        global exception_flag
        global duty_y

        if(duty_y > 2800):
            duty_y = 2800
        if(duty_y < 2000):
            duty_y = 2000

        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            time.sleep(0.5)
            break

        # Run Servo Motor to Right
        if(fin_y > 400):
            duty_y = duty_y - 2
            servo_y.set_servo_pulsewidth(17, duty_y)
            time.sleep(0.05)
        # Run Servo Motor to Left
        elif(fin_y < 300):
            duty_y = duty_y + 2
            servo_y.set_servo_pulsewidth(17, duty_y)
            time.sleep(0.05)
        else:
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
