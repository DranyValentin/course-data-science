#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:06:13 2021

@author: valentin
"""

### 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

with open('task.txt', 'w') as my_file:
    while True:
        my_string = input('Введите строку: ')
        
        if my_string == '':
            break
        
        my_file.write(my_string + '\n')
        
        
        
### 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt') as my_file:
    content = my_file.readlines()

print(f'Файл содержит {len(content)} строк')    
for i in range(len(content)):
    print(f'{i+1} строка, содержит {len(content[i].split())} слова. ')
    
    
### 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open('task3.txt') as my_file:
    content = my_file.readlines()

print('Сотрудники у которых зп менее 20 тыс.:\n')
for line in content:
    arr_line = line.split()
    
    if int(arr_line[1]) < 20000:
        print(f'{line}')
        
        
### 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыри'
}

with open('task4.txt') as my_file:
    with open('new_task_4.txt', 'w') as new_my_file:
        for content in my_file:
            splitedContent = content.split()
            splitedContent[0] = dictionary[splitedContent[0]]
            joinedContent = (' ').join(splitedContent)
            new_my_file.write(f'{joinedContent}\n')
   
        
### 5. Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить ее на экран.
from functools import reduce

with open('task_5.txt', 'w') as my_file:
    my_string = input('Введите числа через пробел: ')
    my_file.write(my_string + '\n')
    
with open('task_5.txt') as my_file:
    content = my_file.readline()
    splitedContent = content.split()
    print(reduce((lambda acc, cur: int(acc) + int(cur)), splitedContent))
    

### 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('task_6.txt') as my_file:
    lessons = []
    
    for content in my_file:
        dictLesson = {}
        lesson = content.split()
        totalHours = 0
        
        for hours in lesson[1:]:
            index = hours.find('(')
            
            if index == -1:
                continue
                
            totalHours += int(hours[:index])
        
        dictLesson[lesson[0][:-1]] = totalHours
        
        lessons.append(dictLesson)

print(lessons)


### 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка:
# [
#   {“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
#   {“average_profit”: 2000}
# ].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.
from functools import reduce
import json

totalProfit = []
firms = {}

with open('task_7.txt') as my_file:
    for content in my_file:
        firm = content.split()
        
        profit = int(firm[2]) - int(firm[3])
        firms[firm[0]] = profit
        
        if profit > 0:
            totalProfit.append(profit)
            
averageProfit =  reduce((lambda acc, cur: acc + cur), totalProfit) / len(totalProfit)
result = [firms, {'average_profit': averageProfit}]

with open("my_file_7.json", "w") as write_f:
    json.dump(result, write_f)

print(result)
        