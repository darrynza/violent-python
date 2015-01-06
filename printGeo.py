# You will need to install the two Ubuntu/Debian packages before you can install GeoIP
# Also, the book references the module as pythongeoip, but it's actually GeoIP
# sudo apt-get install libgeoip-dev
# sudo apt-get install python-dev
# sudo pip install GeoIP

import GeoIP 
gi = GeoIP.GeoIP('/opt/GeoIP/GeoLiteCity.dat', GeoIP.GEOIP_STANDARD)
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	longi = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + tgt + ' Geo-located. '
	print '[+] ' + str(city) + ', ' + str(region) + ', ' + str(country)
	print ' Latitude: ' + str(lat) + ', ' + 'Longitude: ' + str(longi)

tgt = '173.255.226.98'
printRecord(tgt)

