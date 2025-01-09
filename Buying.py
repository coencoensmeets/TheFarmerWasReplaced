from Field import tilt_field, complete_field_carrots_unsafe, intercropping
from Planting import plant_carrot, plant_wheat

def buy_carrot_seeds(N):
	if (num_items(Items.Carrot_Seed)>N):
		return
	if not (num_items(Items.Wood)<N*12+2 or num_items(Items.Hay)<N*12+1):
		trade(Items.Carrot_Seed, N)
		return
	tilt_field()
	print("N: ", N)
	while (num_items(Items.Wood)<N*12+2 or num_items(Items.Hay)<N*12+1):
		print('Intercropping!')
		intercropping(20, [plant_wheat, plant_carrot])
	trade(Items.Carrot_Seed, N)
	tilt_field()

def buy_pumpkin_seeds():
	if (num_items(Items.Pumpkin_Seed)>get_world_size()**2*2):
		return
	if (num_items(Items.Carrot)<get_world_size()**2*5):
		tilt_field()
		complete_field_carrots_unsafe(plant_carrot, get_world_size()*5)
		tilt_field()
	trade(Items.Pumpkin_Seed, get_world_size()**2*5)