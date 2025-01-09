def tilt_field():
	"""
	Tilt the entire field.
	
	This function will tilt the entire field by moving to the top left corner of the field and tilling the soil until the entire field is tilled.
    """
	clear()
	for n in range(get_world_size()):
		for m in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			move(East)
		move(North)