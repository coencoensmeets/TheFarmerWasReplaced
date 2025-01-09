from Planting import plant_tree, plant_carrot, plant_wheat, plant_pumpkin
from Field import tilt_field
from Buying import buy_carrot_seeds, buy_pumpkin_seeds

def intercropping(N, plant_func):
	"""
	Plant N rows of crops in an intercropping pattern.

	Args:
		N: The number of rows to plant.
		plant_func: A list of functions that plant different crops.
	"""
	world_size = get_world_size()
	for i in range(N):
		for j in range(world_size):
			for n in range(world_size):
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					plant_tree()
				else:
					for k in range(len(plant_func), 0 -1):
						if get_pos_y() < world_size//k:
							plant_func[k]()
							break
				move(East)
			move(North)
		
def complete_field(crop):
	"""
	Plant a field of a single crop.

	Args:
		crop: The crop to plant.
	"""
	if crop == Entities.Pumpkin:
		complete_field_pumpkin()
		return
	
	if crop == Entities.Grass:
		complete_field_grass_unsafe(1000000000)
	if crop == Entities.Carrots:
		complete_field_carrots_unsafe(1000000000)

def complete_field_grass_unsafe(N):
	"""
	Plant a field of grass.

	This function is unsafe because it will not check if Grass is ready to harvast. Only use this function if you are sure that the field is ready to harvest.

	Args:
		N: The number of rows to plant.
	"""
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			harvest()
			plant(Entities.Grass)
			move(East)
		move(North)

def complete_field_carrots_unsafe(N):
	"""
	Plant a field of carrots.

	This function is unsafe because it will not check if Carrots are ready to harvast. Only use this function if you are sure that the field is ready to harvest.

	Args:
		N: The number of rows to plant.
	"""
	world_size = get_world_size()
	buy_carrot_seeds(200*world_size)
	for i in range(N/200):
		for j in range(200):
			for n in range(world_size):
				harvest()
				plant(Entities.Carrots)
				move(East)
			move(North)
		trade(Items.Carrot_Seed, 200*world_size)

def complete_field_simple(plant_function, N):
	"""
	Plant a field of a single crop.

	Args:
		plant_function: The function to plant the crop.
	"""
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			plant_function()
			move(East)
		move(North)
		
def complete_field_pumpkin():
	"""
	Plant a field of pumpkins.

	It will make sure that only the biggest pumpkins are harvested.add()

	Todo:
		* Make it so that the function does not keep scanning all cells but only the necessary ones.
	"""
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