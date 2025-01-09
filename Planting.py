def plant_tree():
	if can_harvest() or get_entity_type() == None:
		harvest()
		plant(Entities.Tree)

def plant_carrot():
	if can_harvest() or get_entity_type() == None:
		harvest()
		if (get_ground_type() != Grounds.Soil):
			till()
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)

def plant_wheat():
	if can_harvest() or get_entity_type() == None:
		harvest()
		plant(Entities.Grass)

def intercropping():
	clear()
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
				plant_tree()
			elif get_pos_y() < world_size // 2:
				plant_carrot()
			else:
				plant_wheat()
			move(East)
		move(North)