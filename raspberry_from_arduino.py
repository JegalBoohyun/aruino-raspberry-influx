import serial
import raspberry_to_influxdb

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = ser.readline().split(' ')
    print(data)
    print(raspberry_to_influxdb.send(data[0], data[1], data[2]))

