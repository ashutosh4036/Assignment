import json

class FileHandler:
    def __init__(self, filename="daily_kpi.json"):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def update_kpi(self, date, kpi_data):
        data = self.read_file()
        data[date] = kpi_data
        self.write_file(data)