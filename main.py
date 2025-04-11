with open("data/pokemon-data.json", "r", encoding="utf-8") as f:
    data = f.read()
with open('data/pokemon-sprites.json', 'r', encoding='utf-8') as f:
    sprites = f.read()

import json

data = json.loads(data)
sprites = json.loads(sprites)

from table_aggrid import *
from page_layout import *
from pokemon import *

items = [Pokemon(value, sprites[key]) for key, value in data.items()]

poke_table = Table_NGUI(items=items)
poke_table.column_data['image_url'].type = 'image'
poke_table.select_columns(["image_url", "name", "capture_rate"])
#poke_table.add_filter(lambda pokemon: pokemon.name[0] == "z")
poke_table.run_filters()
print(poke_table)
poke_table.refresh()

'''
with ui.tabs().classes('w-full h-full') as tabs:
    panels = [ui.tab('Pokemon'), ui.tab('2')]

with ui.tab_panels(tabs, value=panels[1]):
    with ui.tab_panel(panels[0]):
        poke_table.update()
'''


ui.run()

