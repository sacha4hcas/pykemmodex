class Column:
    def __init__(self, name, column_type, selected=True):
        self.name = name
        self.type = column_type
        self.selected = selected
        self.max_length = len(name)
        self.label = name.capitalize().replace('_', ' ')
    
    def __str__(self):
        return f"{self.label}"
    
    def __repr__(self):
        return f"{self.name}"

class Table:
    def __init__(self, items=[]):
        self.column_list = []#ordered
        self.column_data = {}
        self.row_data = [] 

        self.filters = []
        self.filtered_index = []

        if (items != []):
            self.add_items(items)
        
    def selected_column_list(self):
        selected_columns = []
        for column in self.column_list:
            if (column.selected == True):
                selected_columns.append(column)
        return selected_columns
    
    def move_column(self, old_pos, new_pos):
        column_to_move = self.column_list[old_pos]
        saved_column = None
        step = 1
        i = new_pos
        if old_pos < new_pos:
            step = -1
        while old_pos != i:
            saved_column = self.column_list[i]
            self.column_list[i] = column_to_move
            column_to_move = saved_column
            i+=step
        self.column_list[i] = saved_column



    def select_columns(self, select_column_names):
        for column in self.column_list:
            if column.name in select_column_names:
                column.selected = True
            else:
                column.selected = False

    def add_item(self, item):
        self.row_data.append(item)
        if not self.column_data:
            self.add_columns_from_object(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def add_filter(self, filter_func):
        self.filters.append(filter_func)

    def run_filters(self):
        self.filtered_index = []
        for i in range(len(self.row_data)):
            if all(f(self.row_data[i]) for f in self.filters):
                self.filtered_index.append(i)

    def add_columns_from_object(self, obj):
        for key, value in obj.__dict__.items():
            if (key[0] != "_") and (type(value) in [int, str, float, bool]):
                self.column_data[key] = Column(
                    name=key,
                    column_type=type(value).__name__,
                    selected=True
                )
                self.column_list.append(self.column_data[key])
    
    def calculate_max_length(self):
        for i in range(len(self.row_data)):
            if i in self.filtered_index:
                item = self.row_data[i]
                for column in self.column_list:
                    column.max_length = max(column.max_length, len(str(getattr(item, column.name))))
    
    def __str__(self):
        self.calculate_max_length()
        _str = ""
        for column in self.column_list:
            if (column.selected):
                padding = column.max_length - len(column.label)
                _str += f'{column.label}{" " * padding} |'
        line_length = len(_str) - 1
        _str += f"\n{line_length * ('-')}\n"

        for i in range(len(self.row_data)):
            if i in self.filtered_index:
                _str += f'{self.row_data[i].table_print(self.column_list)}\n'
           
        return _str
        


    

class PokemonTable(Table):
    def __init__(self):
        pass






