# -*- coding: utf-8 -*-
import datetime
from sense_hat import SenseHat # import sense hat library functions into this program
sense = SenseHat() # define SenseHat() function as sense
sense.clear() # call clear on SenseHat to clear all measurements

import csv

myFile = open('subsurface_sensor_data.csv', 'w')
myFile.close()
guardian=1

while guardian<2:
	
	high_num=20
	low_num =0
	
	for k in range(low_num, high_num):
		# Orientation:
		o = sense.get_orientation() # define call for orientation function of sense hat as of
		# o is located in sense, but also has different parameters attached to it, calling it o tidies up the code		
		sense_data_pitch[k] = o["pitch"] # read pitch parameter of the orientation function, o
		sense_data_roll[k]= o["roll"] # read roll parameter of the orientation function, o
		sense_data_yaw[k]= o["yaw"] # read yaw parameter of the orientation function, o
	
		# Acceleration:
		acceleration = sense.get_accelerometer_raw()
		sense_data_accx[k] = acceleration['x']
		sense_data_accy[k] = acceleration['y']
		sense_data_accz[k] = acceleration['z']
		
		Now=datetime.datetime.utcnow()
		year[k]=Now.year
		month[k]=Now.month
		day[k]=Now.day
		hour[h]=Now.hour
		minute[k]=Now.minute
		second[k]=Now.second
		usecond[k]=Now.microsecond
    
    		###location fetch here###
		
	###DSP CODE HERE-> BELOW IS A PLACEHOLDER###
	filtered_pitch=sense_data_pitch
	filtered_roll=sense_data_roll
	filtered_yaw=sense_data_yaw
	filtered_x=sense_data_accx
	filtered_y=sense_data_accy
	filtered_z=sense_data_accz
	
	myFile = open('subsurface_sensor_data.csv', 'a')
	with myFile:
		
		writer = csv.writer(myFile)
					
		for k in range(len(filtered_pitch)):#all are the same length, so it shouldn't matter which length is used
			senseData = [[filtered_pitch[k], filtered_roll[k], filtered_yaw[k], filtered_x[k], filtered_y[k], filtered_z[k], year[k], month[k], day[k], hour[k], minute[k], second[k], usecond[k]]]	
			writer.writerows(senseData)###future release to also print location###
			
		myFile.close()
		
	guardian=guardian+1
