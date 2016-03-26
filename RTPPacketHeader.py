class RTPPacketHeader:
	
	def create(self):
		self.seq_number = 0
		self.ack_number = 0

		self.src_port = 0
		self.dest_port = 0
		
		self.syn_flag = 0
		self.ack_flag = 0
		self.fin_flag = 0
		self.lst_flag = 0
		self.rst_flag = 0

		self.rcv_window = 0

		self.payload_length = 0

	def toString(self):
		return "" + \
               "Src Port: " + str(self.src_port) + \
               "Dest Port: " + str(self.dest_port) + \
               "Seq #: " + str(self.seq_number) + \
		       "Ack #: " + str(self.ack_number) + \
               "SYN: " + str(self.syn_flag ) + \
               "ACK: " + str(self.ack_flag ) + \
		       "FIN: " + str(self.fin_flag ) +\
               "LST: " + str(self.lst_flag ) + \
               "RST: " + str(self.rst_flag) + \
		       "Payload: " + str(self.payload_length ) + \
               "RCV Win: " + str(self.rcv_window)


	