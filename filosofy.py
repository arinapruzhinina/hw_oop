from multiprocessing import Process, Lock 
from time import sleep
from random import randint

FILOSOFY = 5

class Filosofers(Process):
    TIMEOUT = 1
    
    def __init__(self, name, left_chopstick: Lock, right_chopstick: Lock):
        super().__init__(name=name)
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        
    def food(self):
        print('Философ {} ест'.format(self.name))
        sleep(randint(1, 2))
        print('Философ {} закончил есть и начал думать'.format(self.name))

    def run(self):
        while True:
            if self.left_chopstick.acquire(timeout=Filosofers.TIMEOUT): 
                print('{} философ берет левую палочку'.format(self.name))
                if self.right_chopstick.acquire(timeout=Filosofers.TIMEOUT): 
                    print('{} философ берет правую палочку'.format(self.name))
                    self.food()
                    self.left_chopstick.release()
                    self.right_chopstick.release()
                    sleep(randint(3, 4))
                    print('{} философ хочет есть и не хочет думать'.format(self.name))
                else:
                    self.left_chopstick.release() 

if __name__ == "__main__":
    chopsticks = [Lock() for _ in range(FILOSOFY)]
    for i in range(FILOSOFY):
        leftside = chopsticks[i-1]
        rideside = chopsticks[i]
        Filosofers(str(i), leftside, rideside).start()