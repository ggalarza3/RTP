import socket
from collections import namedtuple

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

MyStruct = namedtuple("MyStruct", "data ACK SEQ windowSize destination")
mess = MyStruct(data = MESSAGE, ACK = 0, SEQ = 0, windowSize = 1, destination = UDP_IP)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(mess, (UDP_IP, UDP_PORT))