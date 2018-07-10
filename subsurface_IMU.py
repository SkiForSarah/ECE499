# -*- coding: utf-8 -*-
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
		pitch = o["pitch"] # read pitch parameter of the orientation function, o
		roll = o["roll"] # read roll parameter of the orientation function, o
		yaw = o["yaw"] # read yaw parameter of the orientation function, o
	
		# Acceleration:
		acceleration = sense.get_accelerometer_raw()
		x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']
		
		sense_data_pitch[k]=pitch
		sense_data_roll[k]=roll
		sense_data_yaw[k]=yaw
		
		sense_data_accx[k]=x
		sense_data_accy[k]=y
		sense_data_accz[k]=z
		
	
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
					
		for k in range(len(filtered_pitch)):
			senseData = [[filtered_pitch[k], filtered_roll[k], filtered_yaw[k], filtered_x[k], filtered_y[k], filtered_z[k]]]	
			writer.writerows(senseData)
			
		myFile.close()
		
	guardian=guardian+1
