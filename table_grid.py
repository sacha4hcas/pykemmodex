from nicegui import ui



class GridTable:
    def __init__(self, table):
        self.columns = {}
        self.table = table

    def addColumn(self, column):
        self.columns.append()
    
    def addRow(self, row):
        for column, value in row.items():
            pass

    def build_ui(self):

        all_columns = ui.row().classes('gap-0')
        with all_columns:
            for column in self.table.column_list:
                ui.label(column.label).classes('border p-1')
