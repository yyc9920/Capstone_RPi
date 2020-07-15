import serial
import time

ser = serial.Serial('/dev/rfcomm0')
ser.isOpen()

crd_x = [0, 0, 0, 0, 0]
crd_y = [0, 0, 0, 0, 0]
cnt = 0

while(1):
    coord = ser.readline()
    coord = coord.decode('utf-8')
    coord = coord[0:-2]

    crd = coord.split('/')
    # crd[0] => crd_x

    tmp = crd[1].split(',')
    # tmp[0] => crd_y, tmp[1] => number of faces
    # end='' => in python, when you use 'print', it automatically change line.
    # end='' makes to use 'print' without changing line.

    print("x = ", end='')
    print(crd[0])
    print("y = ", end='')
    print(tmp[0])
    print("Id = ", end='')
    print(tmp[1])

    time.sleep(0.01)
