# -*- coding: utf-8 -*-
from os import system
import datetime
import GPS_Get

from sense_hat import SenseHat # import sense hat library functions into this program
sense = SenseHat() # define SenseHat() function as sense
sense.clear() # call clear on SenseHat to clear all measurements

import csv

myFile = open('error_distribution_data.csv', 'w')
myFile.close()

#separate function to turn on GPS
#import GPS_Initialize.py
#print('GPS activated')

print('IMU.py is running')
i = 0;
while True:
        i = i + 1
        #write data to file
	myFile = open('error_distribution_data.csv', 'a')
	with myFile:
		
		writer = csv.writer(myFile)
		
		# Time:
		Now = datetime.datetime.utcnow() #get date and time in UTC
		Year = Now.year
		Month = Now.month
		Day = Now.day
		Hour = Now.hour
		Minute = Now.minute
		Second = Now.second
		uSecond = Now.microsecond
		
		#GPS, get UTM coordinates
		try:
                    print('Getting GPS coordinates')
                    reload(GPS_Get)
                    Easting = GPS_Test2.Easting
                    Northing = GPS_Test2.Northing
                    ZoneNumber = GPS_Test2.ZoneNumber
                    ZoneLetter = GPS_Test2.ZoneLetter
		except:
                    print('Unable to get GPS location')
                    Easting = 0
                    Northing = 0
                    ZoneNumber = 0
                    ZoneLetter = '0'
                    
		#print('Getting IMU data')
		# Orientation:			
		o = sense.get_orientation() # define call for orientation function of sense hat as of
			# o is located in sense, but also has different parameters attached to it, calling it o tidies up the code		
		Pitch = o["pitch"] # read pitch parameter of the orientation function, o
		Roll = o["roll"] # read roll parameter of the orientation function, o
		Yaw = o["yaw"] # read yaw parameter of the orientation function, o
						
		# Acceleration:			
		acceleration = sense.get_accelerometer_raw()
		X = acceleration['x']
		Y = acceleration['y']
		Z = acceleration['z']
						
		#x = round(x,0)
		#y = round(y,0)
		#z = round(z,0)
		
		# myFile.write(´%f´ % (pitch))
		senseData = [[Year, Month, Day, Hour, Minute, Second, uSecond, Pitch, Roll, Yaw, X, Y, Z, Easting, Northing, ZoneNumber, ZoneLetter]]
			
		writer.writerows(senseData)
		myFile.close()

