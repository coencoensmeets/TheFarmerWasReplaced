from Planting import plant_tree, plant_carrot, plant_wheat, plant_pumpkin

def tilt_field():
	for n in range(get_world_size()):
		for m in range(get_world_size()):
			till()
			move(East)
		move(North)

def intercropping():
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant_tree()
			elif get_pos_y() < 0:
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
	
	complete_field_simple(plant_func, 10000000)

def complete_field_simple(plant_func, N):
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			plant_func()
			move(East)
		move(North)
		
def complete_field_pumpkin():
	clear()
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
				if (num_items(Items.Carrots)<world_size**2):
					clear()
					complete_field_simple(plant_carrot, 10)
				trade(Items.Pumpkin_Seed, world_size**2*5)
				pumpkin_count = 0
			elif (num_items(Items.Carrots)<world_size**2):
					clear()
					complete_field_simple(plant_carrot, 10)
			else:
				pumpkin_count = 0

			move(East)
		move(North)