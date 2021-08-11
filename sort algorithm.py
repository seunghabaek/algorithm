# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 00:37:09 2021

@author: seungha
"""
#%%
# 선택 정렬 소스코드
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(a)):
    min_idx = a.index(min(a[i:]))
    min_val = min(a[i:])
    a[min_idx], a[i] = a[i], min_val # swap
    
print(a)

# dongbin's
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소가 담길 인덱스
    for j in range(i + 1, len(array)): # 선형 탐색을 통한 최소값 탐
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)

#%%
# 삽입 정렬 알고리즘
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(a)):
    for j in range(i, 0, -1):  # 여기서 idea는 j가 i에따라서 시작point가 달라져야 한다는 점.
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)

#%%
# 퀵 정렬 알고리즘
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소의 갯수가 1일때
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터 찾기
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        # 왼쪽 오른쪽이 엇갈리는 경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)

# list comprehensing이용
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # pivot
    tail = array[1:] # without pivot list
    
    left_side = [x for x in tail if x <= pivot] # left side
    right_side = [x for x in tail if x > pivot] # rght side
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#%%
# 계수 정렬 알고리즘
