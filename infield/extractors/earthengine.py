
SUPPORTS_EARTHENGINE = False
try:
	import ee
	SUPPORTS_EARTHENGINE = True
except ImportError:
	SUPPORTS_EARTHENGINE = False