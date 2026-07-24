import json
from pathlib import Path
from datetime import date


class JSONManager():

    path_to_file:Path
    data:dict[str:int] = {

    }

    def __init__(self, app):
        self.path_to_file = Path(app.user_data_dir) / 'water_cups_data.json'
        # print(f'path_to_file: {self.path_to_file}')

        if not self.path_to_file.exists():
            with open(self.path_to_file, 'w', encoding='utf-8') as file:
                print('Here1')
                self.data[date.today().isoformat()] = 0
                json.dump(self.data, file, ensure_ascii=False, indent=4)
        else:
            print('Here2')
            with open(self.path_to_file, 'r', encoding='utf-8') as file:
                self.data = json.load(file)

    def new_today_data(self, new_cups):
        today = date.today().isoformat()
        if today in self.data.keys():
            self.data[today] += new_cups
        else:
            self.data[today] = new_cups

    def read_today(self):
        return self.data[date.today().isoformat()]

    def write(self, new_cups):
        self.new_today_data(new_cups)
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
