# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.# *Пример:* # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import random
def creat_coeff(n):
    list=[]
    for i in range(n+1):
        list.append(int(random()*100))
    return list


try:
    n=int(input('Введите натуральную степень k для многочлена: '))
    array=creat_coeff(n)
    print(array, 'список коэффициентов')
except ValueError as ex:
    print('Введите число!')
    exit(ex)    


def compose_a_polynomial(array):
    polynomial = ''
    lenght = len(array)
    for i in range(lenght): 
        if i != lenght  and i != lenght - 1 and array[i] != 0:
            polynomial += f'{array[i]}x**{lenght - i - 1}'
            if array[i + 1] != 0:
                polynomial += ' + '
        elif i == lenght - 2 and array[i] != 0: 
            polynomial += f'{array[i]}x'
            if array[i + 1] != 0:
                polynomial += ' + '
        elif i == lenght - 1 and array[i] != 0: 
            polynomial += f'{array[i]} = 0'
        elif i == lenght - 1  and array[i] == 0:
            polynomial += ' =0'          
    return polynomial


import json
BD = compose_a_polynomial(array)
def save():
    with open('BD.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(BD, ensure_ascii=False))
        print('Многочлен успешно сохранен')        
save()

