import serial
import raspberry_to_influxdb

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    value = ser.readline().decode('utf-8')
    data = value.split(' ')
    print(raspberry_to_influxdb.send(int(data[0]), int(data[1]), int(data[2])))

