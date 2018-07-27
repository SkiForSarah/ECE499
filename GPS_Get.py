import serial
import time
import utm

#initialize
ser = serial.Serial("/dev/ttyS0",115200) #start serial

ser.write("AT+CGNSPWR=1\r\n") #power on GPS electronics
PWRcommand = ser.readline() #read command
#print PWRcommand
PWRresponse = ser.readline() #read response
#print PWRresponse
ser.write("AT+CGNSSEQ=\"RMC\"\r\n")# 
SSEQcommand = ser.readline()
#print SSEQcommand
SSEQresponse = ser.readline()
#print SSEQresponse
    
#get coordinates
ser.write("AT+CGNSINF\r\n") #get GPS coordinates
INFcommand = ser.readline()
#print INFcommand
INFresponse = ser.readline()
#print INFresponse
    
#separate by comma
info = INFresponse.split(",") #separate response by commas
Timestamp = info[2]
Latitude = float(info[3])
Longitude = float(info[4])

#uncomment to check
#print "Timestamp:", Timestamp
#print "Latitdue:", Latitude, "degrees N"
#print "Longitude:", Longitude, "degrees E" 
#print("")

#convert to UTM
UTM = utm.from_latlon(Latitude, Longitude)
Easting = UTM[0] #meters East
Northing = UTM[1] #meters North
ZoneNumber = UTM[2] #should be 10
ZoneLetter = UTM[3] #should be U

#uncomment to check
#print("Converted to UTM:")
#print "Easting:", Easting, "mE"
#print "Northing:", Northing, "mN"
#print "Zone: ", ZoneNumber, ZoneLetter
#print("")

ser.close() #close serial
