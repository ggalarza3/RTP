#!/usr/bin/env python
import socket
import sys
from rtp import RTP
from RTPSocket import RTPSocket, SocketState
from RTPPacket import RTPPacket
from RTPPacketHeader import RTPPacketHeader
from RTPException import RTPException

# bring in IP and PORT for socket
TCP_IP, TCP_PORT = sys.argv[1].split(":") 
TCP_PORT = int(TCP_PORT)

# buffer size for information being sent
BUFFER_SIZE = 1024

# setup socket and set to stream for TCP connection
snew = RTP.createRTPSocket(TCP_IP, TCP_PORT)
global snew
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((TCP_IP, TCP_PORT))
except socket.error, msg:
  print "Couldn't connect to server. Closing"
  sys.exit(1)

studentData = []
studentID = sys.argv[2]

# checking if data to search was given
if len(sys.argv) < 4:
  print "No data was asked for"
  sys.exit()

# putting the fields asked for into a list
x = 3
while x < len(sys.argv):
  studentData.append(sys.argv[x])
  x = x + 1

MESSAGE = studentID

# connection established and ready to send ID to check if it exists
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)

# check if ID is present
if data != "ID EXISTS":
  print "This ID does not exist"
  sys.exit()
else:
  # send length of list asked for 
  s.send(str(len(studentData)))
  # receives "Taking Fields"
  data = s.recv(BUFFER_SIZE)
  for a in range(0, len(studentData)): # Send over Fields
    MESSAGE = studentData[a]
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    if data == MESSAGE + ": This field does not exist":
      print data
      sys.exit()

  s.send("Final Call")
  data = s.recv(BUFFER_SIZE)
  data = data[:-3]
  print 'From server: ' + data

s.close()
