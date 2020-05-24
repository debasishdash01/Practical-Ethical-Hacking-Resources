#We will provide an IP and see if ports are open on the IP or a hostname like google.com
#!/usr/bin/env python3

import sys
from datetime import datetime as dt
import socket

if len(sys.argv) == 2: # there will be 2 arguments while we run ' python3 port_scanner.py <IP> '.
                       # port_scanner.py is the first arg and <IP> will be the 2nd argument 
  target = socket.gethostbyname(sys.argv[1]) # translates host to ipv4
else:
  print("Invalid number of args")
  print("Syntax: python3 port_scanner.py [ip/hostname]")

print("Scannning target: " + target) #target is a string here
print("Time started: " + str(dt.now()))
print('-' * 50)

try:
  for port in range(1,65535): #Do a lesser port number so that it will go faster
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5) #when we cant connect to a port its going to wait half-second and then it is going to move on to next port
    
    # if a port is connected the script will return zero, else it will throw an error which trigger one the below line does that
    result = s.connect_ex((target, port)) # error indicator
    
    if result == 0:
      print("port {} is open".format(port))
    s.close 
except KeyboardInterrupt: # interrupts are like ^C to stop
  print('\nExitting...')
  sys.exit()
except socket.gaierror:
  print("Hostname couldn't be resolved")
  sys.exit() #clean exit
except socket.error:
  print("Couldn't connect to server or IP")
  sys.exit()
