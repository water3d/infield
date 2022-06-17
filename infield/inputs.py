
SUPPORTS_GEOPANDAS = False
try:
	import geopandas
	SUPPORTS_GEOPANDAS = True
except ImportError:
	SUPPORTS_GEOPANDAS = False