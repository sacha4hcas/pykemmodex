import os
from nicegui import ui
from table import *

class AggridTable:
    def __init__(self, row_key="name", table=None):
        self.ui_columns = []
        self.ui_rows = []
        self.row_key = row_key

        self.container = None
        self.table_container= None
        self.column_menu_container = None
        self.display_column_menu = True

        self.img_size = (150,150)

        self.table = table
    
    def __enter__(self):
        self.build_ui()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.container:
            self.container.clear()

   

    def build_ui(self):
        if (self.container):
            self.container.clear()
        if (not self.container):
            self.container = ui.row().classes('w-full h-full')
        
        with self.container:
            ui.button('', icon='refresh', on_click=lambda: self.refresh_table())
            ui.button('', icon='menu', on_click = lambda: self.toggle_column_menu())
            self.build_column_menu()
            self.build_table()
            

    def build_table(self):
        if (self.table_container):
            self.table_container.clear()
        if (not self.table_container):
            self.table_container = ui.row().classes('w-full h-full')
        
        with self.table_container:
            self.ui_table = ui.aggrid(
                options={
                    'columnDefs' : self.ui_columns,
                    'rowData': self.ui_rows,
                    'rowHeight': self.img_size[1],
                },
                auto_size_columns=False,
                html_columns=[0]).style("height:800px")
    
    def build_column_menu(self):
        if (self.column_menu_container):
            self.column_menu_container.clear()
        if (not self.column_menu_container):
            self.column_menu_container = ui.row().classes('w-full h-full')
        with self.column_menu_container, ui.grid(columns=10):
                for column in self.table.column_list:
                    ui.switch(column.label, value=column.selected, on_change=lambda e,
                        column=column: self.toggle_column(column, e.value)).classes('border p-2')

    def toggle_column_menu(self):
        self.display_column_menu = not self.display_column_menu
        if (self.display_column_menu):
            self.build_column_menu()
        elif self.column_menu_container:
            self.column_menu_container.clear()

    def update_data(self):
        self.update_columns()
        self.update_rows()
    
    def refresh_table(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{self.table}')
        self.update_data()
        self.build_table()

    def refresh(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{self.table}')
        self.update_data()
        self.build_ui()

   
    def update_columns(self):
        self.ui_columns = []
        for column in self.table.column_list:
            row = {
                "name": column.name,
                "label": column.label,
                "field":column.name,
                "align": "left",
                "hide" : not column.selected
            }
                
            if column.type in ['int', 'float', 'str', 'bool']:
                row['filter'] = 'agTextColumnFilter'
                row['resizable'] = True
                row['autoSizeStrategy'] = {
                    "type" : "fitCellContents"
                }
            elif column.type == 'image':
                row['resizable'] = False
                row['width'] = self.img_size[0]


            if column.name == 'image_url':
                row['lockPosition'] = 'left'

            self.ui_columns.append(row)
        
    
    def update_rows(self):
        self.ui_rows = []
        for i in range(len(self.table.row_data)):
            if i in self.table.filtered_index:
                row = {}
                for column in self.table.column_list:
                    if column.selected:
                        if column.type in ['int', 'float', 'bool', 'str']:
                            row[column.name] = getattr(self.table.row_data[i], column.name)
                        if (column.type == 'image'):
                            img_url = getattr(self.table.row_data[i], column.name)
                            row[column.name] = f'<img src="{img_url}" alt="Image" width="{self.img_size[0]}" height="{self.img_size[1]}">'
                self.ui_rows.append(row)

    def toggle_column(self, column, visible):
        column.selected = visible
        self.ui_table.run_grid_method('setColumnsVisible', [column.name], visible)
        #print(f'column data : {self.column_data}')

