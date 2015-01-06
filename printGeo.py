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

