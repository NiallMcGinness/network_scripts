import paramiko
import sys


args = sys.argv

try:
    ip = args[1]
except IndexError:
    print "no ip provided"
    sys.exit(1)

try:
    username = args[2]
    password = args[3]
    cmd = args[4]
  
except IndexError:
    print "no args provided"
    sys.exit(1)



def runSshCmd(hostname, username, password,cmd,timeout=30):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print hostname
    try:
        client.connect(hostname, port=2222 , username=username, password=password,
                allow_agent=False, look_for_keys=False, timeout=30)

    except (paramiko.SSHException), err:
        print "ssh error : ", err
        client.close()

    channel = client.invoke_shell()
    channel.send(cmd)
    time.sleep(1)
    output = channel.recv(9999)
    client.close()
    return output



print runSshCmd(ip, router_username, router_pwd)