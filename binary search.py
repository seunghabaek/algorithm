# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 00:18:46 2021

@author: seungha
"""
#%%
# binary search

n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # end condition
    if target == array[mid]:
        return mid # index 반환
    # left search
    elif target < array[mid]:
        end = mid - 1
        return binary_search(array, target, start, end)
    # right search
    elif target > array[mid]:
        start = mid + 1
        return binary_search(array, target, start, end)

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1) # index + 1
        