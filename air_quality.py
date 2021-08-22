import serial, time, datetime
serial_path = '/dev/ttyUSB0'
ser = serial.Serial(serial_path)
while True:
    data = []
    for index in range(0, 10):
            datum = ser.read()
            data.append(datum)
    print(datetime.datetime.now())
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little')/10
    print('2.5: {}'.format(pmtwofive))
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little')/10
    print('10: {}'.format(pmten))
    time.sleep(15)
