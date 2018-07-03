# code from here: https://pypi.org/project/utm/
# MIT License so free to use
# download zipped folder from "download files" side tab
# unzip, cd into the resulting "utm-0.4.2" folder
# python setup.py build
# python setup.py install
# (may have to use sudo)
# cd into the "test" folder
# python test_utm.py
# should work from here

import utm

#converting Latitude and Longitude to UTM
Lat = 48.460895
Lon = -123.31089
UTM = utm.from_latlon(Lat, Lon)

print("Easting, Northing, Zone Number, Zone Letter:")
print(UTM)
print("")

#converting UTM to Latitude and Longitude
Easting = 477016
Northing = 5367575
ZoneNumber = 10
ZoneLetter = 'U'
LatLon = utm.to_latlon(Easting, Northing, ZoneNumber, ZoneLetter)

print("Latitude, Longitude:")
print(LatLon)
print("")

