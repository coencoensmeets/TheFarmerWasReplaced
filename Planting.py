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
	harvest()
	plant(Entities.Grass)

def intercropping():
	clear()
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant_tree()
			elif get_pos_y() < 1:
				plant_carrot()
			else:
				plant_wheat()
			move(East)
		move(North)

def plant_one_crop(crop):
	clear()
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if crop == Entities.Grass:
				plant_wheat()
			elif crop == Entities.Carrots:
				plant_carrot()
			move(East)
		move(North)