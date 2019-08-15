from jsongen import *

copy([
	('unique/block_model_chest.json', 'assets/{modid}/models/block/{name}_chest.json'),
	('unique/block_item_chest.json', 'assets/{modid}/models/item/{name}_chest.json'),
	('unique/blockstate_chest.json', 'assets/{modid}/blockstates/{name}_chest.json'),
	('drop_table_generic.json', 'data/{modid}/loot_tables/blocks/{name}_chest.json'),

	('unique/recipe_chest.json', 'data/{modid}/recipes/decoration/crafting/{name}_chest.json')
])