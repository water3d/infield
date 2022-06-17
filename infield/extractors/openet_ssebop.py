SUPPORTS_OPENET_SSEBOP = False
try:
	from openet import ssebop
	SUPPORTS_OPENET_SSEBOP = True
except ImportError:
	SUPPORTS_OPENET_SSEBOP = False
