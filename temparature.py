import os
import glob
import time

# initialize the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# define the path
sensor_path = '/sys/bus/w1/devices/28-0000076026fa/w1_slave'

# function to read the temperature from the sensor
def read_temperature():
    while True:
        try:
            with open(sensor_path, 'r') as f:
                lines = f.readlines()
            if lines[0].strip()[-3:] == 'YES':
                time.sleep(0.2)
                with open(sensor_path, 'r') as f:
                    lines = f.readlines()
                equals_pos = lines[1].find('t=')
                if equals_pos != -1:
                    temp_string = lines[1][equals_pos+2:]
                    temperature = float(temp_string) / 1000.0
                    return temperature
       
while True:
	temperature=read_temperature()
	print('Temparature: {:.2f} C  {:.2f} F' .format(temperature, temperature*9/5+32))
	time.sleep(1)