from Planting import plant_tree, plant_carrot, plant_wheat, plant_pumpkin

def intercropping():
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant_tree()
			elif get_pos_y() < 5:
				plant_carrot()
			else:
				plant_wheat()
			move(East)
		move(North)
		
def complete_field(crop):
	if crop == Entities.Pumpkin:
		complete_field_pumpkin()
		return
	
	if crop == Entities.Grass:
		plant_func = plant_wheat
	elif crop == Entities.Carrots:
		plant_func = plant_carrot
	
	complete_field_simple(plant_func)

def complete_field_simple(plant_func):
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			plant_func()
			move(East)
		move(North)
		
def complete_field_pumpkin():
	world_size = get_world_size()
	pumpkin_count = 0
	plant_mode = True
	while True:
		for n in range(world_size):
			if can_harvest() and get_entity_type() == Entities.Pumpkin and plant_mode:
				pumpkin_count += 1
				if pumpkin_count == world_size**2:
					plant_mode = False
			elif get_entity_type() != Entities.Pumpkin:
				pumpkin_count = 0
				plant_mode = True
				plant_pumpkin()
			elif not plant_mode:
				harvest()
				pumpkin_count = 0

			move(East)
		move(North)