# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 02:06:32 2021

@author: seungha
"""
import math

# 최소 공배수(LCM) 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(a,b))
print(lcm(a,b))
