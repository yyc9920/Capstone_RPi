import serial
import time
import re

ser = serial.Serial('/dev/rfcomm0')
ser.isOpen()

crd_x = [0, 0, 0, 0, 0]
crd_y = [0, 0, 0, 0, 0]
cnt = 0
faceInfo = [0, 0, 0, 0, 0]

while(1):
    coord = ser.readline()
    coord = coord.decode('utf-8')
    coord = coord[0:-2]
    faceNum = coord.split(':')
    # faceNum[0] => crd infos, faceNum[1] => number of faces
    fn = int(faceNum[1])
    if(fn == 1):
        fi1 = faceNum[0][0:-1]
        crd1 = fi1.split('/')
        print("faces = 1")
        print(crd1[0], end='')
        print(crd1)
    elif(fn == 2):
        fi2 = re.split('!', faceNum[0][0:-1])
        crd1 = fi2[0].split('/')
        crd2 = fi2[1].split('/')
        print("faces = 2")
        print(crd1[0], end='')
        print(crd1[1])
        print(crd2[0], end='')
        print(crd2[1])
    elif(fn == 3):
        fi3 = re.split('!|"', faceNum[0][0:-1])
        crd1 = fi3[0].split('/')
        crd2 = fi3[1].split('/')
        crd3 = fi3[2].split('/')
        print("faces = 3")
        print(crd1[0], end='')
        print(crd1)
        print(crd2[0], end='')
        print(crd2)
        print(crd3[0], end='')
        print(crd3)
    elif(fn == 4):
        fi4 = re.split('!|"|#', faceNum[0][0:-1])
        crd1 = fi4[0].split('/')
        crd2 = fi4[1].split('/')
        crd3 = fi4[2].split('/')
        crd4 = fi4[3].split('/')
        print("faces = 4")
        print(crd1[0], end='')
        print(crd1)
        print(crd2[0], end='')
        print(crd2)
        print(crd3[0], end='')
        print(crd3)
        print(crd4[0], end='')
        print(crd4)
    elif(fn == 5):
        fi5 = re.split('!|"|#|$', faceNum[0][0:-1])
        crd1 = fi5[0].split('/')
        crd2 = fi5[1].split('/')
        crd3 = fi5[2].split('/')
        crd4 = fi5[3].split('/')
        crd5 = fi5[4].split('/')
        print("faces = 5")
        print(crd1[0], end='')
        print(crd1)
        print(crd2[0], end='')
        print(crd2)
        print(crd3[0], end='')
        print(crd3)
        print(crd4[0], end='')
        print(crd4)
        print(crd5[0], end='')
        print(crd5)
    time.sleep(0.01)
