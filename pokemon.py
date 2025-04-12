class Pokemon:
    def __init__(self, json_data, sprite_data):
        for (key, value) in json_data.items():
            setattr(self, "image_url", sprite_data['sprites']['front_default'])
            if (type(value) in [int, str, float, bool]):
                setattr(self, key, value)


    def table_print(self, column_list):
        _str = ""
        for column in column_list:
            if column.selected:
                value = getattr(self, column.name)
                padding = column.max_length - len(str(value))
                _str += f'{value}{" " * padding} |'
        return _str
    
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'