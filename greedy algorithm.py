# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 02:32:50 2021

@author: seungha
"""
n = 1260
Count = 0

array = [500, 100, 50, 10]

for coin in array:
    Count += n // coin
    n %= coin
print(Count)