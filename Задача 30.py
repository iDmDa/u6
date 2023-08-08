#Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

pro_count = int(input("Введите количество элементов: "))
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))

def pro_mass(pro_count, a1, d):
    return [a1 + (n-1) * d for n in range(1, pro_count + 1)]

print(pro_mass(pro_count, a1, d))
