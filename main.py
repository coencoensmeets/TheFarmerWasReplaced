from Planting import plant_bushes, plant_carrots, plant_wheat, crop_to_plant

while True:
	N=20
	
	crop = crop_to_plant()
	
	if crop == Entities.Grass:
		plant_wheat(N)
	elif crop == Entities.Carrots:
		plant_carrots(N)
	else:
		plant_bushes(N)