# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:46:00 2021

@author: seungha
"""


# permutations
from itertools import permutations

data = ['A','B','C']

result = list(permutations(data,3))   # 3개를 뽑음
print(result)


#%%
# combinations
from itertools import combinations

data = ['D', 'E', 'F']

result = list(combinations(data, 2))   # 2개를 뽑음
print(result)


#%%
# product - 중복 순열
from itertools import product

data = ['A','B','C']

result = list(product(data, repeat=2))
print(result)

#%%
# combination_with_replacement -  중복조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)

