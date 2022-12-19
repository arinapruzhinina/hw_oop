import csv 
from typing import Tuple

class Building:
    def __init__(self, numb_floors: int|float, height: int|float, lenght: int|float, name:str):
        self.numb_floors = numb_floors
        self.height = height 
        self.length = lenght
        self.name = name 

    @classmethod 
    def from_tuple(cls, data: Tuple[str]):
        return cls(data[0], data[1], data[2], data[3])
    
    def to_tuple(self):
        return self.numb_floors, self.height, self.length, self.name

    def __str__(self):
        return(f"\
            Количество этажей: {self.numb_floors}, \
            Высота здания: {self.height}, \
            Длина здания: {self.length}, \
            Имя здания: {self.name}")

if __name__ == '__main__':        
    with open('buildings', 'rt') as file:
        csv_in = csv.reader(file)
        buildings = [Building.from_tuple(building) for building in csv_in]

    for building in buildings:    
        print(building)
