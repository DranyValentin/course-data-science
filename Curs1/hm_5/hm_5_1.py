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

with open('task.txt') as my_file:
    content = my_file.readlines()

print(f'Файл содержит {len(content)} строк')    
for i in range(len(content)):
    print(f'{i+1} строка, содержит {len(content[i].split())} слова. ')
    
    
### 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open('task.txt') as my_file:
    content = my_file.readlines()

  
print(f'Сотрудники у которых зп менее 20 тыс.:\n')
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

with open('task.txt') as my_file:
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
import os
import sys

with open('task.txt_5', 'w') as my_file:
    my_string = input('Введите числа через пробел: ')
    my_file.write(my_string + '\n')
    
with open('task.txt_5') as my_file:
    content = my_file.readline()
    splitedContent = content.split()
    print(reduce((lambda acc, cur: int(acc) + int(cur)), splitedContent))
    
os.path.abspath(__file__)
a = sys.argv[0]

import inspect
src_file_path = inspect.getfile(lambda: None)