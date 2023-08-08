#Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума). Список можно задавать рандомно
#
#На входе : [ 1, 5, 88, 100, 2, -4]
#33
#200
#Ответ: [2, 3]

import random

print("\033c", end="")

def rnd_gen(min, max, count) :
    return [random.randint(min, max) for _ in range(count)]

def find_number(list, dia_min, dia_max) :
    return [count for count, i in enumerate(list) if (i > dia_min and i < dia_max)]

list = rnd_gen(-10, 150, 10)
print(list)

print(find_number(list, int(input("Введите начало диапазона: ")), 
                        int(input("Введите конец диапазона: "))))

