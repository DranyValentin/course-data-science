#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:52:19 2021

@author: valentin
"""

### 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        result = ''
        
        for el in self.matrix:
            result += ', '.join(str(x) for x in el) + '\n'
    
        return f'{result}'
    
    def __add__(self, other):
        sum = []
        
        for index, elements in enumerate(self.matrix):
            sum.append([])
            
            for i, el in enumerate(elements):

                sum[index].append(el + other.matrix[index][i])
        
        return Matrix(sum)
        
    
l = [[1,2,3], [4,5,6]]
l1 = [[1,2,3], [4,5,6]]
matrix1 = Matrix(l)
matrix2 = Matrix(l1)

print(matrix1 + matrix2)

### 2. Реализовать проект расчета суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая может
# иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить
# работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def getFabricConsumption(self):
        pass
    
class Coat(Clothes):
    def __init__(self, V):
        self.V = V
        
    @property
    def getFabricConsumption(self):
        return self.V / 6.5 + 0.5
    
class Suit(Clothes):
    def __init__(self, H):
        self.H = H
        
    @property
    def getFabricConsumption(self):
        return 2 * self.H + 0.3
    
coat = Coat(6.5)
print(coat.getFabricConsumption)

suit = Suit(6.5)
print(suit.getFabricConsumption)