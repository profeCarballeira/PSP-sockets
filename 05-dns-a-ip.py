import socket

try:
  #host = 'www.amazon.es'
  #host = socket.getfqdn() 
  host = 'A30PC01'
  print ("IP de %s: %s" %(host,socket.gethostbyname(host)))
except socket.error as msg:
  print ("%s: %s" %(host, msg))