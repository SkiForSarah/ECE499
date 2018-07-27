# -*- coding: utf-8 -*-
import time
print('5 second delay to ^C')
time.sleep(5)

from os import system
from os.path import exists
import datetime
import csv

try:
    import GPS_Get #import function that gets GPS coordinates
except Exception as e:
    print('*** could not initilize GPS first time, error: ***')
    print(e)

from sense_hat import SenseHat # import sense hat library functions into this program
sense = SenseHat() # define SenseHat() function as sense
sense.clear() # call clear on SenseHat to clear all measurements

#create name for data file
dateT = datetime.datetime.utcnow()
dateStr = str(dateT.year) + str(dateT.month) + str(dateT.day) + '_' + str(dateT.hour) + str(dateT.minute) + 'h'
fileName = 'surface_data' + dateStr + '_0.csv' #change to "subsurface_data" for drogue
while exists(fileName): #if file by this name already exists
	index = int(fileName[fileName.rfind('_')+1:fileName.rfind('.')])
	index = index + 1
	fileStart = fileName[:fileName.rfind('_')+1]
	fileName = fileStart + str(index) + '.csv' #add index number to end of file name

print('saving data to ' + fileName)

myFile = open(fileName, 'w') #create data file
myFile.close()

print('IMU.py is running')
StopFlag = 0
try:
    while StopFlag != 1:
            #write data to file
            myFile = open(fileName, 'a')
            with myFile:
                    
                    writer = csv.writer(myFile) #create file writer
                    
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
                        print('getting GPS coordinates')
                        reload(GPS_Get)
                        Easting = GPS_Get.Easting
                        Northing = GPS_Get.Northing
                        ZoneNumber = GPS_Get.ZoneNumber
                        ZoneLetter = GPS_Get.ZoneLetter
                    except:
                        #could be because GPS_Get failed to import first time
                        try:
                            import GPS_Get.py #try to import GPS_Get again
                        except Exception as e:
                            print('*** could not import again, error: ***')
                            print(e)
                            
                        #otherwise, probably a connection issue
                        print('*** unable to get GPS location ***')
                        Easting = 0
                        Northing = 0
                        ZoneNumber = 0
                        ZoneLetter = '0'
                        
                    #orientation		
                    o = sense.get_orientation() # define call for orientation function of sense hat as of
                            # o is located in sense, but also has different parameters attached to it, calling it o tidies up the code		
                    Pitch = o["pitch"] # read pitch parameter of the orientation function, o
                    Roll = o["roll"] # read roll parameter of the orientation function, o
                    Yaw = o["yaw"] # read yaw parameter of the orientation function, o
                                                    
                    #acceleration			
                    acceleration = sense.get_accelerometer_raw()
                    X = acceleration['x']
                    Y = acceleration['y']
                    Z = acceleration['z']
                    
                    #write data to file
                    senseData = [[Year, Month, Day, Hour, Minute, Second, uSecond, Pitch, Roll, Yaw, X, Y, Z, Easting, Northing, ZoneNumber, ZoneLetter]]     
                    writer.writerows(senseData)
                    myFile.close()
                    
except KeyboardInterrupt: #if interrupted by ^C
    print('keyboard interrupt, setting StopFlag = 1')
    StopFlag = 1; #will stop the while True: loop
    

