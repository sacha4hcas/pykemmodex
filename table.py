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
        return f"{self.type}"

class Table:
    def __init__(self, items=[]):
        self.column_data = {}
        self.row_data = [] 

        self.filters = []
        self.filtered_index = []

        if (items != []):
            self.add_items(items)
        
    
    def select_columns(self, columns):
        for column_name, data in self.column_data.items():
            if column_name in columns:
                data.selected = True
            else:
                data.selected = False

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
    
    def calculate_max_length(self):
        for i in range(len(self.row_data)):
            if i in self.filtered_index:
                item = self.row_data[i]
                for column_name, data in self.column_data.items():
                    data.max_length = max(data.max_length, len(str(getattr(item, column_name))))
    
    def __str__(self):
        self.calculate_max_length()
        _str = ""
        for column_name, data in self.column_data.items():
            if (data.selected):
                padding = data.max_length - len(data.label)
                _str += f'{data.label}{" " * padding} |'
        line_length = len(_str) - 1
        _str += f"\n{line_length * ('-')}\n"

        for i in range(len(self.row_data)):
            if i in self.filtered_index:
                _str += f'{self.row_data[i].table_print(self.column_data)}\n'
           
        return _str
        


    

class PokemonTable(Table):
    def __init__(self):
        pass






