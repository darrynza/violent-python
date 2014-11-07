import optparse
import pxssh

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[-] Error connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output + '\n'

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
uid = 'root'
pwd = '8812P6xe'

addClient('kali1', uid, pwd)
addClient('kali2', uid, pwd)
addClient('kali3', uid, pwd)
botnetCommand('down')
# botnetCommand('apt-get update')
