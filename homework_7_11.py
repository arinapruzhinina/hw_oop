import math

class NotValidTriangle(Exception):
    pass 

class Triangle:

    def __init__(self, first_side: float, second_side: float, third_side: float ) -> None:
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if not self.is_valid():
            raise NotValidTriangle

    def perimetr(self) -> float:
        return round((self.first_side + self.second_side + self.third_side), 3)

    def area(self) -> float:
        p = (self.first_side + self.second_side + self.third_side) / 2
        return round((p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side)) ** 0.5, 3)
    def is_valid(self) -> bool:
        all_sides = sorted([self.first_side, self.second_side, self.third_side])
        for side in all_sides:
            if not isinstance(side, float|int):
                return False 
            if side <= 0:
                return False
        if all_sides[2] > all_sides[0] + all_sides[1]: # треугольник существует если сумма двух любых сторон больше третьей
            return False 
        return True

class NotValidCircle(Exception):
    pass 

class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius 
        if not self.is_valid():
            raise NotValidCircle

    def length(self) -> float:
        return round(2 * math.pi * self.radius, 3)
    
    def area(self) -> float:
        return round(math.pi * self.radius ** 2, 3)
    
    def is_valid(self) -> bool:
        if isinstance(self.radius, float|int):
            return self.radius > 0





d = Circle(5)
print(d.length(), d.area())
