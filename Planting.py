def plant_bushes(N):	
	clear()
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			move(East)
		move(North)

def plant_carrots(N):
	clear()
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			if can_harvest():
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
			move(East)
		move(North)

def plant_wheat(N):
	clear()
	world_size = get_world_size()
	for i in range(N):
		for n in range(world_size):
			if can_harvest():
				harvest()
				plant(Entities.Grass)
			move(East)
		move(North)

def crop_to_plant():
	N_wheat = num_items(Items.Hay)
	N_carrot = num_items(Items.Carrot)
	N_bush = num_items(Items.Wood)

	if N_wheat < N_carrot and N_wheat < N_bush:
		return Entities.Grass
	elif N_carrot < N_wheat and N_carrot < N_bush:
		return Entities.Carrots
	else:
		return Entities.Bush