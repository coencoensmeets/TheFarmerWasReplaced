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

def plant_pumpkin():
		if (get_ground_type() != Grounds.Soil):
			till()
		if (num_items(Items.Pumpkin_Seed) == 0):
			trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)