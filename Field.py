def tilt_field():
	clear()
	for n in range(get_world_size()):
		for m in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			move(East)
		move(North)