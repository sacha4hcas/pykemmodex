from nicegui import ui
grid = ui.grid(columns=3).classes("w-full gap-0")
with grid:
    
    ui.label("")
    ui.label("name").classes('border p-1')

    ui.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/649.png").style("height:100px;width:100px")
    ui.label("pokémon").classes('border p-1')
    
    ui.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/646.png").style("height:100px;width:100px")
    with ui.grid(columns=2):
        ui.label("sublabel1").classes('border p-1')
        ui.label("sublabel2").classes('border p-1')
        ui.label("subvalue1").classes('border p-1')
        ui.label("subvalue2").classes('border p-1')
ui.run()