import serial
import time
import utm

#initialize
ser = serial.Serial("/dev/ttyS0",115200)
ser.write("AT+CGNSPWR=1\r\n")
PWRcommand = ser.readline()
#print PWRcommand
PWRresponse = ser.readline()
#print PWRresponse
ser.write("AT+CGNSSEQ=\"RMC\"\r\n")
SSEQcommand = ser.readline()
#print SSEQcommand
SSEQresponse = ser.readline()
#print SSEQresponse
    
#get coordinates
ser.write("AT+CGNSINF\r\n")
INFcommand = ser.readline()
#print INFcommand
INFresponse = ser.readline()
#print INFresponse
    
#separate by comma
info = INFresponse.split(",")
Timestamp = info[2]
Latitude = float(info[3])
Longitude = float(info[4])

#print "Timestamp:", Timestamp
#print "Latitdue:", Latitude, "degrees N"
#print "Longitude:", Longitude, "degrees E" 
#print("")

#convert to UTM
UTM = utm.from_latlon(Latitude, Longitude)
Easting = UTM[0]
Northing = UTM[1]
ZoneNumber = UTM[2]
ZoneLetter = UTM[3]

#print("Converted to UTM:")
#print "Easting:", Easting, "mE"
#print "Northing:", Northing, "mN"
#print "Zone: ", ZoneNumber, ZoneLetter
#print("")

