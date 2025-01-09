from Planting import plant_tree, plant_carrot, plant_wheat, plant_pumpkin


def tilt_field():
	clear()
	for n in range(get_world_size()):
		for m in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			move(East)
		move(North)

def intercropping():
	tilt_field()
	world_size = get_world_size()
	while True:
		for n in range(world_size):
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant_tree()
			elif get_pos_y() < world_size//2:
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
	buy_pumpkin_seeds()
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
				buy_pumpkin_seeds()
				pumpkin_count = 0
			else:
				pumpkin_count = 0

			move(East)
		move(North)

def buy_pumpkin_seeds():
	if (num_items(Items.Pumpkin_Seed)>get_world_size()**2*2):
		return
	if (num_items(Items.Carrot)<get_world_size()**2*5):
		tilt_field()
		complete_field_simple(plant_carrot, get_world_size()*5)
		tilt_field()
	trade(Items.Pumpkin_Seed, get_world_size()**2*5)