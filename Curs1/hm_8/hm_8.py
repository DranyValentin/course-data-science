#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:52:19 2021

@author: valentin
"""

### 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date
        
    @classmethod
    def getDay(cls, Date):
        day = int(Date.date.split('-')[0])
        
        if cls.validateDay(cls, day):
            return day
        
        return False
    
    @classmethod
    def getMonth(cls, Date):
        month = int(Date.date.split('-')[1])
        
        if cls.validateMonth(cls, month):
            return month
        
        return False
    
    @classmethod
    def getYear(cls, Date):
        year = int(Date.date.split('-')[2])
        
        if cls.validateYear(cls, year):
            return year
        
        return False
    
    @staticmethod
    def validateDay(cls, day):
        if day > 0 and day < 32:
            return True
        
        return False
    
    @staticmethod
    def validateMonth(cls, month):
        if month > 0 and month < 13:
            return True
        
        return False
    
    @staticmethod
    def validateYear(cls, year):
        if len(str(year)) == 4:
            return True
        
        return False
    
date = Date('13-12-2022')
print(f'Day: {Date.getDay(date)}')
print(f'Month: {Date.getMonth(date)}')
print(f'Year: {Date.getYear(date)}')

date1 = Date('213-212-20222')
print('\n')
print(f'Bad Day: {Date.getDay(date1)}')
print(f'Bad Month: {Date.getMonth(date1)}')
print(f'Bad Year: {Date.getYear(date1)}')


### 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __init__(self, text):
        self.text = text
        
print('Для завершения работы введите -1')
        
while True:
    val1 = int(input('Введите делимое: '))
    val2 = int(input('Введите делитель: '))
    
    if val1 == -1 or val2 == -1:
        break
    try:
        if val2 == 0:
            raise MyException('Делить на 0 нельзя')
            
        print(f'Частное: {val1 / val2}')
        print('\n')
    except MyException as err:
        print(err)
        
        
### 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения на
# реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список. Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только
# числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение. При этом работа
# скрипта не должна завершаться.
class MyException(Exception):
    def __init__(self, text):
        self.text = text
        
class MyList:
    def __init__(self):
        self.list = []
        
    def add(self, element):
        try:
            if (element.isdigit()):
                self.list.append(int(element))
            else:
                raise MyException("Введенное значение не число")
        except MyException as err:
            print(err)
                
    def __str__(self):
        return ', '.join([str(x) for x in self.list])
                    
    
myList = MyList()
        
while True:
    number = input('Введите число, для завершения ввода введите stop: ')
    
    if number == 'stop':
        break
    
    myList.add(number)
    
print(myList)

### 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

### 5. Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

class Sklad:
    def __init__(self):
        self.productList = []
        
    def add(self, Product):
        self.productList.append(Product)
        
    def subtract(self, Product):
        print(type(Product))
        product = [product for product in self.productList if product.name == Product.name and type(product) == type(Product)]
        
        if product[0].amount > 0:
            product[0].amount -= 1
            return True
        
        return False
        
        
class Product:
    amount = 0
    
    def __init__(self, name, price, category):
        self.name = name
        self.category = category
        self.price = price
        self.amount += 1
        
    def setAmount(self, amount):
        self.amount = amount
    
    
class Printer(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 'office equipment')

        
class Scanner(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 'office equipment')
        
class Copier(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 'office equipment')
        
printer = Printer('HP', 1000)
scanner = Scanner('HP', 2000)
copier = Copier('HP', 3000)

sklad = Sklad()

sklad.add(printer)
sklad.add(scanner)
sklad.add(copier)

printer.setAmount(5)
print(sklad.subtract(printer))
print(sklad.subtract(scanner))
print(sklad.subtract(scanner))

print(sklad.productList)


### 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, realPart, imaginaryPart):
        self.realPart = realPart
        self.imaginaryPart = imaginaryPart
        
    def __add__(self, other):
        return ComplexNumber(self.realPart + other.realPart, self.imaginaryPart + other.imaginaryPart)
    
    def __mul__(self, other):
        rVal1 = self.realPart * other.realPart
        iVal1 = self.realPart * other.imaginaryPart
        rVal2 = self.imaginaryPart * other.imaginaryPart * -1
        iVal2 = self.imaginaryPart * other.realPart
        
        return ComplexNumber(rVal1 + rVal2, iVal1 + iVal2)
    
    def __str__(self):
        return f'RealPart: {self.realPart}\nImaginaryPart: {self.imaginaryPart}i'
        
c1 = ComplexNumber(1, -1)
c2 = ComplexNumber(3, 6)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)