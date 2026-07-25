import json
from pathlib import Path
from datetime import date


class JSONManager():
    '''
    Класс для работы с файлом water_cups_data.json 
    Информация о выпитых кружках.
    ''' 

    path_to_file:Path = Path()
    data:dict[str:int] = {}

    def __init__(self, app):
        '''
        Конструктор.
        
        Производится проверка на существование файла.
        '''
        self.path_to_file = Path(app.user_data_dir) / 'water_cups_data.json'
        print(f'path_to_file: {self.path_to_file}')

        if not self.path_to_file.exists():
            with open(self.path_to_file, 'w') as file:
                self.data[date.today().isoformat()] = 0
                json.dump(self.data, file, indent=4)
        else:
            with open(self.path_to_file, 'r') as file:
                self.data = json.load(file)

    def new_today_data(self, new_cups):
        '''
        Запись -> прибавление новых выпитых кружек.
        
        Проверка на существование текущей даты.
        '''
        today = date.today().isoformat()
        if today in self.data.keys():
            self.data[today] += new_cups
        else:
            self.data[today] = new_cups

    def read_today(self):
        '''
        Чтение текущего количество выпитых кружек из data.
        
        Проверка на наличие текущей даты.
        '''
        today = date.today().isoformat()
        if today in self.data.keys():
            return self.data[today]
        else:
        	self.data[today] = 0
        	return self.data[today]

    def write(self, new_cups):
        '''
        Запись обновлённых данных в файл.
        '''
        self.new_today_data(new_cups)
        with open(self.path_to_file, 'w') as file:
            json.dump(self.data, file, indent=4)
