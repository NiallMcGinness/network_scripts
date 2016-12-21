import sys
import telnetlib
import socket
import json 

args = sys.argv

try:
    ip = args[1]
except IndexError:
    print "no ip provided"
    sys.exit(1)

try:
    username = args[2]
except IndexError:
    print "no username provided"
    sys.exit(1)

try:
    password = args[3]
except IndexError:
    print "no password provided"
    sys.exit(1)

try:
    cmd = args[4]
except IndexError:
    print "no command for smart rg provided"
    sys.exit(1)

ports = [23,2323]

def checkports(ip,ports):
    s = socket.socket()
    openPorts = []
    for port in ports:
        try:
            s.connect((ip, port))
            openPorts.append(port)
        except Exception as e: 
            e
        finally:
            s.close()
    return openPorts


def sendCommand(ip, username, password, port, cmd):
    output = None
    tn = telnetlib.Telnet()
    tn.open(ip, port, timeout=30)
    tn.read_until("Login:")
    tn.write(username +  "\r\n")
    tn.read_until("Password:")
    tn.write(password +  "\r\n")
    tn.read_until(">")
    tn.write(cmd)
    time.sleep(1)
    output = tn.read_very_eager()
    tn.write("exit")
    tn.close()
    return output



openPortArray = checkports(ip,ports)


if len(openPortArray) > 0:
    port = openPortArray[0]
    output = sendCommand(ip, username, password, port, cmd)
    

print output
    
    