import serial
import time

ser = serial.Serial('/dev/rfcomm0')
ser.isOpen()

while(1):
	coord = ser.readline()
	coord = coord.decode('utf-8')
	coord = coord[0:-4]
	crd = coord.split('/')
	crd_x = float(crd[0])
	crd_y = float(crd[1])
	print("x = ", end='')
	print(crd_x)
	print("y = ", end='')
	print(crd_y)
	time.sleep(0.1)
