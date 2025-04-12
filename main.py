with open("data/pokemon-data.json", "r", encoding="utf-8") as f:
    data = f.read()
with open('data/pokemon-sprites.json', 'r', encoding='utf-8') as f:
    sprites = f.read()

import json

data = json.loads(data)
sprites = json.loads(sprites)

from table_aggrid import *
from table_grid import *
from page_layout import *
from pokemon import *

items = [Pokemon(value, sprites[key]) for key, value in data.items()]

poke_table = Table(items=items)


poke_table.column_data['image_url'].type = 'image'
poke_table.select_columns(["image_url", "name", "capture_rate"])
poke_table.add_filter(lambda pokemon: pokemon.name[0] == "z")
poke_table.run_filters()
print(poke_table)

aggrid_table = GridTable(table=poke_table)
aggrid_table.build_ui()

ui.run()

