import socket

import RTPPacket
import pickle

class SocketState:
	CREATED = "created",
	BIND = "bind",
	CONNECTED = "connected",
	CLOSED = "closed",


CONNECTION_TIMEOUT_LIMIT = 1
LISTEN_TIMEOUT_LIMIT = 100
RECEIVE_TIMEOUT_LIMIT = 20

class RTPSocket:
	CONNECTION_TIMEOUT_LIMIT = CONNECTION_TIMEOUT_LIMIT
	LISTEN_TIMEOUT_LIMIT = LISTEN_TIMEOUT_LIMIT
	RECEIVE_TIMEOUT_LIMIT = RECEIVE_TIMEOUT_LIMIT

	def __init__(self):
		print("Creating new RTPSocket")
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.state = SocketState.CREATED
		self.send_window = 1
		self.receive_window_size = RTPPacket.MAX_WIN

		self.source_address = None
		self.destination_address = None 

		self.seq_number = 0
		self.ack_number = 0

		self._socket.settimeout(CONNECTION_TIMEOUT_LIMIT * 5)

		print("Socket created!", str(self))

	def bind(self, source_address):
		self.source_address = self.source_address or source_address
		self._socket.bind(self.source_address)
		self.state = SocketState.BIND
		print("Socket has been bound! ", str(self))

	def close(self):
		print("Closing socket: ", str(self))
		self._socket.close()
		self.state = SocketState.CLOSED
		print("Socket closed!", str(self))

	def setTimeout(self, value):
		self._socket.settimeout(value)

	def connect(self, destination_address):
		# if not self.state == SocketState.BIND:
		# 	raise RxPException("Socket not bound yet")
		# elif self.state == SocketState.CONNECTED:
		# 	raise RxPException("Socket already connected")

		self.destination_address = destination_address
		self.state = SocketState.CONNECTED

	def sendPacket(self, rtp_packet):

		self._socket.sendto(rtp_packet.toBytes(), self.destination_address)

	def receivePacket(self, rcv_win_size):
		self._socket.settimeout(CONNECTION_TIMEOUT_LIMIT)
		while True:
			try:
				packet, address = self._socket.recvfrom(int(rcv_win_size))
				print "packet received"
				packet = self.unpicklePacket(packet)
				packet_type = type(packet)
				if not isinstance(packet, RTPPacket.RTPPacket):
					print("Incorrect packet type!.  Received: ", packet_type)
					continue

				print "unpickled"

				break
			except Exception as e:
				print("Received error", e)
				raise e

		print "Returning packet"
		return (address, packet)

	@property
	def timeout(self):
		return self._socket.gettimeout()
	@timeout.setter
	def timeout(self, time):
		self._socket.settimeout(time)

	def unpicklePacket(self, packet):
		return pickle.loads(packet)

		
	def __str__(self):
		return "Current state: " + str(self.state[0]) + ", Current src: " + str(self.source_address) \
			+ ", Current dst: " + str(self.destination_address)