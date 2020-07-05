import serial
import threading
import time
import RPi.GPIO as GPIO
from pathlib import Path

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22,GPIO.OUT)
servo1 = GPIO.PWM(22,50) # Note 11 is pin, 50 = 50Hz pulse

servo1.start(0)
time.sleep(1)

b_device = Path("/dev/rfcomm0")

# Coordinates x, y
crd_x = [0, 0, 0, 0, 0]
crd_y = [0, 0, 0, 0, 0]
cnt = 0
fin_x = 0
fin_y = 0
tmp = [0, 0]
duty = 2

exception_flag = 0

def getCoord():
    while True:
        global b_device
        global crd_x
        global crd_y
        global cnt
        global fin_x
        global fin_y
        global exception_flag

        if(b_device.exists() == True):
            #Read Coordinates String via Bluetooth Communication
            try:
                ser = serial.Serial('/dev/rfcomm0')
                coord = ser.readline()
                coord = coord.decode('utf-8')
                coord = coord[0:-2]
            except serial.serialutil.SerialException as e:
                print(e)
                print("Bluetooth connection lost")
                exception_flag = 1
                break
            else:
                pass
            crd = coord.split('/')
            tmp = crd[1].split(',')
            # tmp[0] => crd_y, tmp[1] => number of faces
        else:
            continue

        tmp_x = int(crd[0])
        tmp_y = int(tmp[0])

        # end='' => change line in python

        if(tmp[1] == '1'):
            crd_x[4] = 0
            crd_y[4] = 0
            crd_x[3] = 0
            crd_y[3] = 0
            crd_x[2] = 0
            crd_y[2] = 0
            crd_x[1] = 0
            crd_y[1] = 0
            crd_x[0] = tmp_x
            crd_y[0] = tmp_y
            print("Face ", end='')
            print(cnt+1)
            print("x = ", end='')
            print(crd_x[cnt])
            print("y = ", end='')
            print(crd_y[cnt])
        
        if(tmp[1] == '2'):
            crd_x[4] = 0
            crd_y[4] = 0
            crd_x[3] = 0
            crd_y[3] = 0
            crd_x[2] = 0
            crd_y[2] = 0
            if(cnt == 0):
                crd_x[0] = tmp_x
                crd_y[0] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 1):
                crd_x[1] = tmp_x
                crd_y[1] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            
            cnt += 1
            if(cnt == 2):
                cnt = 0
        
        if(tmp[1] == '3'):
            crd_x[4] = 0
            crd_y[4] = 0
            crd_x[3] = 0
            crd_y[3] = 0
            if(cnt == 0):
                crd_x[0] = tmp_x
                crd_y[0] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 1):
                crd_x[1] = tmp_x
                crd_y[1] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 2):
                crd_x[2] = tmp_x
                crd_y[2] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            
            cnt += 1
            if(cnt == 3):
                cnt = 0
        
        if(tmp[1] == '4'):
            crd_x[4] = 0
            crd_y[4] = 0
            if(cnt == 0):
                crd_x[0] = tmp_x
                crd_y[0] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 1):
                crd_x[1] = tmp_x
                crd_y[1] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 2):
                crd_x[2] = tmp_x
                crd_y[2] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 3):
                crd_x[3] = tmp_x
                crd_y[3] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            
            cnt += 1
            if(cnt == 4):
                cnt = 0
        
        if(tmp[1] == '5'):
            if(cnt == 0):
                crd_x[0] = tmp_x
                crd_y[0] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 1):
                crd_x[1] = tmp_x
                crd_y[1] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 2):
                crd_x[2] = tmp_x
                crd_y[2] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 3):
                crd_x[3] = tmp_x
                crd_y[3] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            elif(cnt == 4):
                crd_x[4] = tmp_x
                crd_y[4] = tmp_y
                print("Face ", end='')
                print(cnt+1)
                print("x = ", end='')
                print(crd_x[cnt])
                print("y = ", end='')
                print(crd_y[cnt])
            
            cnt += 1
            if(cnt == 5):
                cnt = 0
        
        tmpcnt = int(tmp[1])
        fin_x = (crd_x[0] + crd_x[1] + crd_x[2] + crd_x[3] + crd_x[4])/tmpcnt
        fin_y = (crd_y[0] + crd_y[1] + crd_y[2] + crd_y[3] + crd_y[4])/tmpcnt

def runServo():
    while True:
        global servo1
        global fin_x
        #global fin_y
        global exception_flag
        global duty
    
        if(exception_flag == 1):
            print("test")
            exception_flag = 0
            duty = 7
            servo1.ChangeDutyCycle(duty)
            time.sleep(0.5)
            break

        if(fin_x >= 100 and fin_x <= 150):
            duty = 2
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 151 and fin_x <= 200):
            duty = 2.625
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 201 and fin_x <= 250):
            duty = 3.25
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 251 and fin_x <= 300):
            duty = 3.875
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 301 and fin_x <= 350):
            duty = 4.5
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 351 and fin_x <= 400):
            duty = 5.125
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 401 and fin_x <= 450):
            duty = 5.75
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 451 and fin_x <= 500):
            duty = 6.375
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 501 and fin_x <= 550):
            duty = 7
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 551 and fin_x <= 600):
            duty = 7.625
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 601 and fin_x <= 650):
            duty = 8.25
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 651 and fin_x <= 700):
            duty = 8.875
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 701 and fin_x <= 750):
            duty = 9.5
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 751 and fin_x <= 800):
            duty = 10.125
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 801 and fin_x <= 850):
            duty = 10.75
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 851 and fin_x <= 900):
            duty = 11.375
            servo1.ChangeDutyCycle(duty)
        elif(fin_x >= 900):
            duty = 12
            servo1.ChangeDutyCycle(duty)

#set getCoord to Therad
def getCoord_therad():
    thread=threading.Thread(target=getCoord)
    thread.daemon=True
    thread.start()

#Main
while True:
    if(b_device.exists() == True):
        getCoord_therad()
        runServo()
    else:
        print("Bluetooth not connected.")
        print("Sleep 5 seconds")
        time.sleep(5)