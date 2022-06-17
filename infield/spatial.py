"""
	Instantiate the corrct object to handle spatial operations - e.g. finding extent, or maybe iterating objects?
	Some of the spatial operations may depend on where we're sending the data, so there will be some interplay between
	these objects and the extractors.
"""


class SpatialItems(object):
	pass


class GeopandasSpatialItems(SpatialItems):
	pass


class CoordinatePairsSpatialItems(SpatialItems):
	"""
		Will we actually use this, or have a GeopandasSpatialItems.from_coordinate_pairs() constructor method?
	"""
	pass