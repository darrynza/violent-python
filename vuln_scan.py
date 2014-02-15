import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable'
    elif 'Blah' in banner:
        print '[+] Blah is vulnerable'
    else:
        print '[-] FTP Server is not vulnerable'
    return

def main():
    # ip1 = '192.168.1.133'
    # ip2 = '192.168.1.1'
    # port = 21
    portList = [21,22,23,25,80,110,443]
    for x in range(1, 255):
	 	ip = '192.168.1.' + str(x)
		print "Checking %s" % (ip)
		for port in portList:
			banner = retBanner(ip, port)
    		if banner:
				print '[+]' + ip + ': ' + banner
				checkVulns(banner)

if __name__ == '__main__':
    main()

