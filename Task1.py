# задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def prime_number(n):
    for i in range(2,int(n*0.5)):
        if n % i==0:                   # проверяем есть ли в отрезке число, на которое делится n без остатка
            return False
    return True       


def factorization(n):
    fact=[]
    fact2=[]
    for i in range(2,int(n*0.5)):
        while n % i ==0:
            fact.append(i)
            n/=i 
    if prime_number(n) == True: 
        fact2.append(1)
        fact2.append(n)                  
    return fact or fact2


try:
    n=int(input('Ввведите целое натуральное число: '))
    if n!=1:
        res=factorization(n)
        print(res, 'простые множетели числа')
        res1=prime_number(n)
        if res1 == True:
            print('Число ', n, 'является простым!!')    
    else:
        print('Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.')  
except ValueError as ex:
    print('Введите число!')
    exit(ex)   
