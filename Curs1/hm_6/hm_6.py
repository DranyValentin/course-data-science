#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:52:19 2021

@author: valentin
"""

### 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = 'green';
    
    def running(self):
        while True:
            print(f'Light: {self.__color}')
            if self.__color == 'green':
                sleep(10)
                self.__color = 'red';
            elif self.__color == 'yellow':
                sleep(2)
                self.__color = 'green';
            elif self.__color == 'red':
                sleep(7)
                self.__color = 'yellow';
                
trafficLight = TrafficLight()
trafficLight.running()


### 2. Реализовать класс Road (дорога), в котором определить
# атрибуты: length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см
# толщины полотна. Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т
# depth = 5 # initial coverage depth (in sm)
# mass_per_sq_m = 25 # initial mass per square meter (in kg)

class Road:
    __length = 0
    __width = 0
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def getWeightAsphalt(self, mass_per_sq_m, depth):
        return (self.__length * self.__width * mass_per_sq_m * depth) / 1000
    
road = Road(20, 5000)
road.getWeightAsphalt(25, 5)


### 3. Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход). Последний
# атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
# Position (должность) на базе класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income
        
    def getProfit(self):
        return self.__income['wage'] + self.__income['bonus']
        
class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    
    def get_total_income(self):
        return self.getProfit()
        
position = Position('Андрей', 'Шевченко', 'директор', {"wage": 1000, "bonus": 200})
print('Full name', position.get_full_name())
print('Profit:', position.get_total_income())


### 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.

class Car:
    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = is_police
        
    def go(self):
        self.speed = 10
        print(f'Auto {self.name} go.')
        
    def stop(self):
        self.speed = 0
        print(f'Auto {self.name} stop.')
        
    def turn(self, direction):
        print(f'Auto {self.name} turn {direction}.')
        
    def show_speed(self):
        print(f'Auto {self.name} speed {self.speed}')
        
    def addSpeed(self):
        self.speed += 10


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def addSpeed(self):
        super().addSpeed()
        
        if self.speed > 60:
            super().show_speed()
            print(f'Attention! Your speed very high!')
            
class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def addSpeed(self):
        super().addSpeed()
        
        if self.speed > 40:
            super().show_speed()
            print(f'Attention! Your speed very high!')

townCar = TownCar('Mazda', 'red')
townCar.go()
townCar.show_speed()
townCar.turn('left')
townCar.addSpeed()
townCar.show_speed()
townCar.addSpeed()
townCar.show_speed()
townCar.addSpeed()
townCar.show_speed()
townCar.addSpeed()
townCar.show_speed()
townCar.addSpeed()
townCar.show_speed()
townCar.addSpeed()
townCar.stop()



### 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print(f'Run draw')
        
class Pen(Stationery):
    def __init__(self):
        super().__init__('pen')
        
    def draw(self):
        super().draw()
        print(f'Draw {self.title}')
        
class Pencil(Stationery):
    def __init__(self):
        super().__init__('Pencil')
        
    def draw(self):
        super().draw()
        print(f'Draw {self.title}')
                
class Handle(Stationery):
    def __init__(self):
        super().__init__('Handle')
        
    def draw(self):
        super().draw()
        print(f'Draw {self.title}')
        
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()