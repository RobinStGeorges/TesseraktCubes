import serial
ser = serial.Serial('/dev/ttyUSB0',115200)
ser.write('{'+'0'+';'+'3'+';'+'125'+';'+'255'+';'+'3'+';}')
print ('sent')