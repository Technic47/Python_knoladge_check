from Record import Record


class Cache:
    records = []

    def __init__(self, new_records: []):
        self.records = new_records

    def add_record(self, value: Record) -> None:
        # global records
        self.records.insert(value.get_id(), value)

    def del_record(self, item: Record):
        # global records
        index = self.records.index(item)
        self.records.pop(index)

    def update_record(self, old_rec: Record, new_rec: Record):
        index = self.records.index(old_rec)
        self.records.pop(index)
        self.records.insert(index, new_rec)

    def get_records(self) -> list:
        return self.records

    def sort(self) -> None:
        self.records.sort()
