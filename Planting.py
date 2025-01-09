def plant_tree():
	"""
	Plant a tree if possible otherwise harvest the field.
	"""
	if can_harvest() or get_entity_type() == None:
		harvest()
		plant(Entities.Tree)

def plant_carrot():
	"""
	Plant carrots if possible otherwise harvest the field.
	"""
	if can_harvest() or get_entity_type() == None:
		harvest()
		trade(Items.Carrot_Seed)
		plant(Entities.Carrots)
	elif get_entity_type() != Entities.Carrots:
		harvest()
		plant(Entities.Carrots)

def plant_wheat():
	"""
	Plant wheat if possible otherwise harvest the field.
	"""
	if can_harvest() or get_entity_type() == None:
		harvest()
		plant(Entities.Wheat)

def plant_pumpkin():
	"""
	Plant pumpkins.
	"""
	plant(Entities.Pumpkin)