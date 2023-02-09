from database_controller import Controller


class Worker:
    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        while True:
            match input():
                case 'add':
                    print("Enter you record: ")
                    rec = input()
                    self.controller.save_record(rec)
                    print('Record saved!')

                case 'view':
                    print('Your records: ')
                    for item in self.controller.all_records():
                        print(str(item.get_id()) + ' ' + str(item.get_date()) + ' ' + item.get_text())

                case 'save':
                    self.controller.save(self.controller.db_path)
                    print("Saved")

                case 'load':
                    self.controller.load()
                    print('Loaded')

                case 'del':
                    print('Enter index of record witch you want to delete: ')
                    index = input()
                    answer = self.controller.del_record(int(index))
                    if answer:
                        print("Record deleted")
                    else:
                        print("Wrong id!")

                case 'update':
                    print('Enter index of record witch you want to update: ')
                    index = input()
                    print('Enter new record text: ')
                    text = input()
                    answer = self.controller.edit_record(int(index), text)
                    if answer:
                        print("Record updated")
                    else:
                        print("Wrong id!")

                case 'exit':
                    raise SystemExit
                case _:
                    print('Wrong command, try again!')
