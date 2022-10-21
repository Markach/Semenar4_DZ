from distutils.cmd import Command
from random import *
import json  
capital={}

def save():
    with open('capital.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(capital,ensure_ascii=False))
    print('Список стран был успешно сохранен в файле capital.json')

def load():
    with open('capital.json', 'r', encoding='utf-8') as fh:
        capital=json.load(fh)
    print('Список был успешно загружен ')
    

try:
    with open('capital.json', 'r', encoding='utf-8') as fh:
        capital=json.load(fh)
    print('Список был успешно загружен ')    
except:
    capital={}
    capital['Колумбия'] = 'Богота'
    capital['Венесуэла'] = 'Kаракас'
    capital['Норвегия'] = 'Осло'
    capital['Сирия'] = 'Дамаск'
    capital['Кения'] = 'Найроби'
    capital['Австралия'] = 'Канберра'
    capital['Канада'] = 'Оттава'
    capital['Швейцария'] = 'Берн'
    capital['Индонезия'] = 'Джакарта'

print('Команда start для начала работы ')
while True:
    command=input('Введите команду ')
    if command=='start':
        print('Бот-столицы стран начал свою работу')
        print('Список мин команд для работы: /all список пар страна-столица, /stop остановить работу бота /add добавить связку(страна-столица) для изучения')
    elif command =='/stop':
        save()
        print('Бот остановил свою работу. Заходите еще, будем рады!')
        break  
    elif command =='/all':
        print('Вот текущий список столиц стран: ')
        print(capital)
    elif command =='/add':
          key=input('введите название страны, которую нужно добавить: ')
          capital[key]=input('введите название столицы, которую нужно добавить: ')
          print('Пара страна-столица успешно добавлена в коллекцию!')
    elif command=='help':
        print('здесь какой-то манул')
    elif command=='/delete':
        key=input('введите название страны, которую нужно удалить: ')
        try:
            del capital[key]
            print('Страна успешно удалена!')
        except KeyError:
            print('В базе нет страны с таким названием!') 
    elif command=='/find':
        key=str.capitalize(input('введите название страны,столицу которую нужно найти: '))
        val='Страны нет в базе'
        print(capital.get(key, val))  
    elif command =='/save':
        save()  
    elif command =='/load':
        with open('capital.json', 'r', encoding='utf-8') as fh:
            capital=json.load(fh)
        print('Список был успешно загружен ')
    
    else:
        print('Неопознанная команда. Просьба погладить манула через /help')   