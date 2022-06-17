SUPPORTS_OPENET_API = False
try:
	import openet_client
	SUPPORTS_OPENET_API = True
except:
	SUPPORTS_OPENET_API = False