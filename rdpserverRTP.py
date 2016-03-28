#!/usr/bin/env python

import socket
import sys
from rtp import RTP
from RTPSocket import RTPSocket, SocketState
from RTPPacket import RTPPacket
from RTPPacketHeader import RTPPacketHeader
from RTPException import RTPException
import threading


TCP_IP = '0.0.0.0'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 20  # Normally 1024, but we want fast response


#create/bind
global snew
snew = RTP.createRTPSocket(TCP_IP, TCP_PORT)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
in_conn = RTP.listenForRTPConnections(snew)
#s.listen(1)

students = []
students.append({
  'ID' : '903076259', # Are these sets?
  'first_name' : 'Anthony',
  'last_name' : 'Peterson',
  'quality_points' : 231,
  'gpa_hours' : 63,
  'gpa' : 3.666667
})
students.append({
  'ID' : '903084074', # Are these sets?
  'first_name' : 'Richard',
  'last_name' : 'Harris',
  'quality_points' : 236,
  'gpa_hours' : 66,
  'gpa' : 3.575758
})
students.append({
  'ID' : '903077650', # Are these sets?
  'first_name' : 'Joe',
  'last_name' : 'Miller',
  'quality_points' : 224,
  'gpa_hours' : 65,
  'gpa' : 3.446154
})

checkFor = []



while 1:
    rtp.acceptRTPSocketConnection(snew, incoming)
    if rtp.isConnected(snew):
        thread = threading.Thread(target=listenForServerRequests)
        thread.start()
        threads.append(thread)
    #conn, addr = s.accept()

    data = rtp.receiveData()
    #data = conn.recv(BUFFER_SIZE)

    if not data :
        here = 'await data'
    else :
      messageBack = "This ID does not exist"
      for w in range(0, len(students)):
        if (data == students[w]['ID']):
          messageBack = "ID EXISTS"
          IDINDEX = w
          break
      ######conn.send(messageBack)  # echo
      rtp.sendData(snew, messageBack)
      if messageBack == 'ID EXISTS':
        ####lstLength = conn.recv(BUFFER_SIZE)
        lstLength = rtp.receiveData()
        ####conn.send("Taking Fields")
        rtp.sendData(snew, "Taking Fields")
        errorMsg = ''
        # create list of asked for fields
        for a in range(0, int(lstLength)):
          ####data = conn.recv(BUFFER_SIZE)
          data = rtp.receiveData()
          if (data not in students[w]):
            errorMsg = data + ": This field does not exist"
            checkFor = []
            ####conn.send(errorMsg)
            rtp.sendData(snew, errorMsg)
            break
            #sys.exit()
          else:
            checkFor.append(data)
            ####conn.send("Received: " + data)
            rtp.sendData(snew, "Received: " + data)
        #create dictionary to print responses
        if not errorMsg:
          ####conn.recv(BUFFER_SIZE)
          rtp.receiveData()
          LASTMESSAGE = ''
          i = 0
          for i in range(0, int(lstLength)):
            LASTMESSAGE += checkFor[i] + ': ' + str(students[IDINDEX][checkFor[i]]) + ', '
          LASTMESSAGE += "\n"
          checkFor = []
          #messageBack = ""
          ####conn.send(LASTMESSAGE)
          rtp.sendData(snew, LASTMESSAGE)


rtp.closeRTPSocket(snew) 

def listenForServerRequests():
  print "Listening for server requests!"
  while(True):
      data = rtp.receiveData(snew)
      #if "GET" in str(request):
      #    print "GETTING a file"
      #    request = str(request).replace("GET: ", "")
      #    print "Getting file: ", request

      #with open (request, "r") as myfile:
      #    data = myfile.read()

      rtp.sendData(snew, data)
#conn.close()

