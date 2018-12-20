import logging

class VcsClass :
	"""Class to describe Incoming Parameters of a CPL from a Cisco VCS 
	"""

	def __init__(self, parameter):
		self.logger = logging.getLogger('')
		self.__parameter = str(parameter)
		if :
			pass
		print listOutput


	def getData(self, rank):
	"""Method Share by some other method to get the required substring
	"""
		message = request.get_data(cache=False)
		message = message.split("&")
		value = message[rank].split("=")
		return value[2] 	
	

	def ALLOW_INTERWORKING(self):
	"""Value is TRUE/False
	"""
		listOutput = self.getdata(0)
		return listOutput

	def AUTHENTICATED(self):
	"""Value is TRUE/False
	"""	
		listOutput = self.getdata(1)
		return listOutput

	def AUTHENTICATED_SOURCE_ALIAS(self):
		if self.AUTHENTICATED == "TRUE":
			listOutput = self.getData(2)
		else:
			listOutput = "User Not AUTHENTICATED"
		return listOutput

	def AUTHENTICATION_USER_NAME(self):
		if self.AUTHENTICATED == "TRUE":
			listOutput = self.getData(3)
		else:
			listOutput = self.getdata(2)
		return listOutput

	def CLUSTER_NAME(self):
		if self.AUTHENTICATED == "TRUE":
			listOutput = self.getdata(4)
		else:
			listOutput = self.getdata(3)	
		return listOutput

	def DESTINATION_ALIAS(self):
		listOutput = self.getdata(4)
		return listOutput

	def DESTINATION_ALIAS_PARAMS(self):
		listOutput = self.getdata(5)
		return listOutput

	def GLOBAL_CALL_SERIAL_NUMBER(self):
		listOutput = self.getdata(6)
		return listOutput

	def LOCAL_CALL_SERIAL_NUMBER(self):
		listOutput = self.getdata(7)
		return listOutput

	def METHOD(self):
	"""Value is INVITE / ARQ / LRQ / OPTIONS / SETUP
	"""	
		listOutput = self.getdata(9)
		return listOutput

	def NETWORK_TYPE(self):
	"""Value is IPV4 / IPV6
	"""	
		listOutput = self.getdata(10)
		return listOutput

	def POLICY_TYPE(self):
	"""Value is SEARCH / ADMIN
	"""
		listOutput = self.getdata(11)
		return listOutput

	def PROTOCOL(self):
	"""Value is SIP / H323
	"""
		listOutput = self.getdata(12)
		return listOutput

	def REGISTERED_ALIAS(self):
		listOutput = self.getdata(12)
		return listOutput

	def SOURCE_ADDRESS(self):
		listOutput = self.getdata(0)
		return listOutput

	def SOURCE_IP(self):
		listOutput = self.getdata(0)
		return listOutput

	def SOURCE_PORT(self):
		listOutput = self.getdata(0)
		return listOutput

	def TRAVERSAL_TYPE(self):
	"""Value is TYPE_[UNDEF / ASSENTSERVER / ASSENTCLIENT /	H460SERVER / H460CLIENT / TURNSERVER / TURNCLIENT / ICE]
	"""
		listOutput = self.getdata(0)
		return listOutput
		
	def UNAUTHENTICATED_SOURCE_ALIAS(self):
		listOutput = self.getdata(0)
		return listOutput

	def UTCTIME(self):
		listOutput = self.getdata(0)
		return listOutput

	def ZONE_NAME(self):
		listOutput = self.getdata(0)
		return listOutput
