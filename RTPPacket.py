# noinspection PyUnresolvedReferences
from RTPPacketHeader import RTPPacketHeader
import pickle
import math

MAX_PAYLOAD = math.pow(2,9) # bytes
MAX_RESEND = math.pow(2,5)
MAX_WIN = math.pow(2, 16)
MAX_PACK_SIZE = math.pow(2,10)

class RTPPacket:
	MAX_PAYLOAD = MAX_PAYLOAD
	MAX_RESEND = MAX_RESEND
	MAX_WIN = MAX_WIN
	MAX_PACK_SIZE = MAX_PACK_SIZE

	def create(self, header=None, payload=None):
		self.header = header or RTPPacketHeader()
		self.payload = payload
		if self.payload is None or self.payload == None:
			self.payload = '_'
		self.header.payload_length = len(self.payload)

	def toBytes(self):
		return pickle.dumps(self)

	def toStr(self):
		print("Packet payload: ", self.payload)
