import zipfile
from threading import Thread

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "Password cracked. Exiting.."
		return password
	except:
		return

def main():
	zFile =zipfile.ZipFile('all.zip')
	passFile = open('dict.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()

if __name__ == "__main__":
	main()
 

