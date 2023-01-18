from multiprocessing import Process, Queue, Event, Lock
from time import sleep
from random import randint, choice
from faker import Faker

class Client:
    def __init__(self, name: str, service: str):
        self.name = name
        self.service = service

class Hairdresser:
    TIME_WAIT = 10
   
    def __init__(self, services):
        self.client_came = Event()
        self.services = services

    def sleep(self):
        print('Парикмахер спит')
        return  self.client_came.wait(timeout=Hairdresser.TIME_WAIT)

    def call(self):
        self.client_came.set()

    def service(self, client: Client):
        print('Парикмахер выполняет услугу {} для клиента {}'.format(client.service, client.name))
        sleep(randint(3, 6))
                
    def greet(self, client: Client):
        self.client_came.clear()
        self.service(client)
        print('Клиент {} готов'.format(client.name))


class Salon:

    def __init__(self, database, q_size: int, locker: Lock):
        self.database = database
        self.q_size = q_size
        self.locker = locker
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Hairdresser(database)
        self.__process = Process(target=self.work)

    def open(self):
        print('Салон открылся и {} человек сидят в очереди'.format(self.q_size))
        self.__process.start()

    def close(self):
        print('Салон закрыт')

    def work(self):
        while True:
            self.locker.acquire()
            if self.__queue.empty():
                self.locker.release()
                work_result = self.__worker.sleep()
                if not work_result:
                    self.close()
                    break
            else:
                self.locker.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client):
        with locker:
            print('Клиент {} зашел в салон'.format(client.name))
            if self.__queue.full():
                print('Клиент {} увидел огромную очередь и ушел домой'.format(client.name))
            else:
                print(f'Клиент {client.name} хочет {client.service}')
                self.__queue.put(client)
                self.__worker.call()

SIZE_QUEUE = 2
CLIENT_ENTER_INTERVAL = (1, 2)
SERVICE = ['стрижка', 'укладка', 'окрашивание']

if __name__ == '__main__':
    locker = Lock()
    fake = Faker()
    names = [fake.name() for _ in range(10)]
    clients = [Client(name, choice(SERVICE)) for name in names]
    salon = Salon([SERVICE], SIZE_QUEUE, locker)
    salon.open()
    for client in clients:
        sleep(randint(*CLIENT_ENTER_INTERVAL))
        salon.enter(client)