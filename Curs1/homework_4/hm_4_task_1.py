#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:30:07 2021

@author: valentin
"""

### 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, pricePerHour, bonus = argv


def getSalary(hours, pricePerHour, bonus):
    return (hours * pricePerHour) + bonus



print('\nЗаработаная плата сотрудника, составляет: ', getSalary(float(hours), float(pricePerHour), float(bonus)))
