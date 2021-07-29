# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 02:02:59 2021

@author: seungha
"""
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['red'])

print(dict(counter))