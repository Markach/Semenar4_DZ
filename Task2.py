#задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import random

def creat_list(n):
    list=[]
    for i in range(n):
        list.append(int(random()*15))
    return list

try:
    x=int(input('Ввведите натуральное число: '))
    array=creat_list(x)
    print(array, 'исходная последoвательность')
except ValueError as ex:
    print('Введите число!')
    exit(ex)    

array1=set(array)   # преобразуем в множество(т.к. в нем только уникальные элементы)
print(list(array1), 'список неповторяющихся элементов исходной последовательности')
