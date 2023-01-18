from threading import Thread, Condition, Lock
from time import sleep
from random import randint, choice
from string import ascii_lowercase as lc

text = ''
class Pisately(Thread):
    
    def __init__(self, name):
        super().__init__(name=name)
      
    def run(self):
        global text
        while True:
            with lock:
                text = ''
                print(f'Писатель {self.name} начинает писать книгу')
                if not text:
                    for _ in range (5):
                        text = text + choice(lc)
                        sleep(randint(1, 4))
                        condition.acquire()
                        condition.notify_all()
                        condition.release()
                print(f'Писатель {self.name} перестал писать книгу')
            sleep(randint(1, 3))
class Chitately(Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global text
        while True:
            with condition:
                print("{} читатель читает ".format(self.name), text)
                condition.wait()
       
if __name__ == "__main__":
    condition = Condition()
    lock = Lock()
    for nums in range(2): 
        Pisately(str(nums)).start()
    for nums in range(4):
            Chitately(str(nums)).start()