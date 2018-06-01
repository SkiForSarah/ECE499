# -*- coding: utf-8 -*-
import datetime
from sense_hat import SenseHat # import sense hat library functions into this program
sense = SenseHat() # define SenseHat() function as sense
sense.clear() # call clear on SenseHat to clear all measurements

import csv

myFile = open('sensor_data.csv', 'w')
myFile.close()

while True:
	myFile = open('sensor_data.csv', 'a')
	with myFile:
		
		writer = csv.writer(myFile)
		
		# Orientation:
					
		o = sense.get_orientation() # define call for orientation function of sense hat as of
			# o is located in sense, but also has different parameters attached to it, calling it o tidies up the code
					
		pitch = o["pitch"] # read pitch parameter of the orientation function, o
		roll = o["roll"] # read roll parameter of the orientation function, o
		yaw = o["yaw"] # read yaw parameter of the orientation function, o
						
		# Acceleration:
						
		acceleration = sense.get_accelerometer_raw()
		x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']
						
		x = round(x,0)
		y = round(y,0)
		z = round(z,0)
		
		# Time:
		Now = datetime.datetime.utcnow() #get date and time in UTC
		Year = Now.year
		Month = Now.month
		Day = Now.day
		Hour = Now.hour
		Minute = Now.minute
		Second = Now.second
		uSecond = Now.microsecond
						 
		# myFile.write(´%f´ % (pitch))
		senseData = [[pitch, roll, yaw, x, y, z, Year, Month, Day, Hour, Minute, Second, uSecond]]
			
		writer.writerows(senseData)
		myFile.close()
