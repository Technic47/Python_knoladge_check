from datetime import datetime


class Record:
    id = int
    date = datetime
    text = ''

    def __init__(self, id: int, date: datetime, text: str):
        self.id = id
        self.date = date
        self.text = text

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> datetime:
        return self.date

    def get_text(self) -> str:
        return self.text

    def __eq__(self, other):
        return self.id == other.id

    def __key(self):
        return self.id, self.date, self.text

    def __hash__(self):
        return hash(self.__key())

    def __lt__(self, other):
        return self.id < other.id
