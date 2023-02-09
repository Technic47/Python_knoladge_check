import database_controller
from worker import Worker


def start():
    controller = database_controller.Controller('newfile.csv')
    worker = Worker(controller)
    worker.start()


if __name__ == '__main__':
    print('Hello!!')
    start()
