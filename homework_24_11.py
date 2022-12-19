import csv 
from homework_24_11_2 import Building

print('Введите количество этажей в здании: ', end='')
k = input()
print('Введите высоту здания: ', end='')
h = input()
print('Введите длину здания: ', end='')
l = input()
print('Введите имя здания: ', end='')
n = input()

try:
    k, h, l = int(k), int(h), int(l) 
except ValueError:
    print('Неправильный тип данных')
else:
    if k > 0 and h > 0 and l > 0:
        bs = Building(k, h, l, n)
        with open ('buildings', 'a') as file:
                csv_out = csv.writer(file)
                csv_out.writerow(bs.to_tuple())
    else:
        print('Дом не смог создаться ;(')
