import requests

SUPPORTS_THREDDS_SIPHON = False
SUPPORTS_THREDDS_REST = True

try:
	import siphon
	SUPPORTS_THREDDS_SIPHON = True
except ImportError:
	SUPPORTS_THREDDS_SIPHON = False