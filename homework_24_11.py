import csv 
from typing import Tuple

class Bilding:
    def __init__(self, numb_floors: int|float, hight: int|float, lenght: int|float, name:str):
        self.numb_floors = numb_floors
        self.hight = hight 
        self.length = lenght
        self.name = name 

    # def to_tuple(self):
    #     return(self.numb_floors, self.hight, self.length, self.name)
    
    @classmethod 
    def from_tuple(cls, data: Tuple[str]):
        return cls(data[0], data[1], data[2], data[3])
    
    def __str__(self):
        return(f"\
            Количество этажей: {self.numb_floors}, \
            Высота здания: {self.hight}, \
            Длина здания: {self.length}, \
            Имя здания: {self.name}")

print('Введите количество этажей в здании: ', end='')
k = input()
print('Введите высоту здания: ', end='')
h = input()
print('Введите длину здания: ', end='')
l = input()
print('Введите имя здания: ', end='')
n = input()

bs = Bilding(k, h, l, n)

try:
    if int(k) > 0 and int(h) > 0 and int(l) > 0:
        with open ('bildings', 'a') as file:
            # csv_out = csv.DictWriter(file, ['количество этажей', ' высота', 'длина', 'имя'])
            # csv_out.writeheader()
            csv_out = csv.writer(file)
            csv_out.writerow([bs.numb_floors, bs.hight, bs.length, bs.name])
        print('Вы создали дом!')
    else:
        print('Дом не смог создаться')

except ValueError:
    print('Вы ввели неправильный тип данных')

with open('bildings', 'rt') as file:
    csv_in = csv.reader(file)
    bildings = [Bilding.from_tuple(bilding) for bilding in csv_in]

for bilding in bildings:    
    print(bilding)
