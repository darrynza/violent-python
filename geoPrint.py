import dpkt
import socket
import GeoIP
import optparse

gi = GeoIP.GeoIP('/opt/GeoIP/GeoLiteCity.dat', GeoIP.GEOIP_STANDARD)
def retGeoStr(ip):
	try:
		rec = gi.record_by_name(ip)
		city = rec['city']
		country = rec['country_code3']
		if city != '':
			geoLoc = city + ', ' + country
		else:
			geoLoc = country
		return geoLoc
	except Exception, e:
		return 'Unregistered'

def printPcap(pcap):
	print "printPcap subroutine. Input is %s\n" % (pcap)
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_nota(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] Src: ' + src + ' --> Dst: ' + dst
			print '[+] Src: ' + regGeoStr(src) + ' -->Dst: ' \
				+ retGeoStr(dst)
		except:
			pass

def main():
	parser = optparse.OptionParser('usage%prog -p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type='string', \
		help='specify pcap filename')
	(options, args) = parser.parse_args()
	if options.pcapFile == None:
		print parser.usage
		exit(0)
	pcapFile = options.pcapFile
	print pcapFile 	
	f = open(pcapFile)
	pcap = dpkt.pcap.Reader(f) 
   print "%d\n" % (len(pcap))	
	printPcap(pcap)

if __name__ == '__main__':
	main()
