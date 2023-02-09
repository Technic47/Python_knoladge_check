import csv
from datetime import datetime
from os.path import exists

from Cache import Cache
from Record import Record


class Controller:
    cache = Cache([])
    id = int

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        if exists(db_path):
            self.id = self.get_last_id()
            self.load()
        else:
            self.create_file()
            self.id = 1

    def get_last_id(self) -> int:
        with open('id_count.txt', 'r') as file:
            symbol = file.read()
            number = int(symbol)
        return number

    def set_last_id(self, value: int):
        with open('id_count.txt', 'w') as idfile:
            idfile.write(str(value))

    def create_file(self):
        with open(self.db_path, 'w', newline='') as csvfile:
            fieldnames = ['id', 'date', 'record']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def save(self, path: str):
        with open(path, 'w') as csvfile:
            fieldnames = ['id', 'date', 'record']
            writer = csv.DictWriter(csvfile, delimiter=':', fieldnames=fieldnames)
            writer.writeheader()
            for item in self.all_records():
                writer.writerow({'id': item.get_id(), 'date': item.get_date(), 'record': item.get_text()})
            self.set_last_id(self.id)

    def load(self):
        if exists(self.db_path):
            pass
        else:
            self.create_file()
        with open(self.db_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=':')
            for line in reader:
                record = Record(int(line['id']), line['date'], line['record'])
                self.cache.add_record(record)
        self.cache = Cache(list(set(self.cache.get_records())))
        self.cache.sort()

    def save_record(self, text: str):
        record = Record(self.id, datetime.now(), text)
        self.id += 1
        self.cache.add_record(record)

    def del_record(self, id: int) -> bool:
        item = self.get_record(id)
        if item is not None:
            self.cache.del_record(item)
            return True
        else:
            return False

    def edit_record(self, id: int, text: str) -> bool:
        item = self.get_record(id)
        if item is not None:
            new_item = Record(item.get_id(), item.get_date(), text)
            self.cache.update_record(item, new_item)
            return True
        else:
            return False

    def all_records(self) -> list:
        return self.cache.get_records()

    def get_record(self, id: int) -> Record | None:
        for item in self.cache.get_records():
            if item.get_id() == id:
                return item
        return None

    def __del__(self):
        self.save('backup.csv')
        print("BackUp done!")
