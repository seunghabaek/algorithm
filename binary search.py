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
        
#%%
# python binary search library

from bisec import bisec_left, bisec_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisec_left(a, x))
print(bisec_right(a, x))

#%%
# 값이 특정 범위에 속하는 데이터의 갯수 구하기

from bisect import bisect_left, bisect_right

def count_by_range(array, start, end):
    left_index = bisect_left(array, start)
    right_index = bisect_right(array, end)
    
    return right_index - left_index

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# find value = 4
print(count_by_range(array, 4, 4))

# find range (-1, 3) values
print(count_by_range(array, -1, 3))

#%%
# 떡볶이 떡 만들기

n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# binary search
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in array:
        # 클 때만 자르기
        if x > mid:
            total += (x - mid)
    # left search
    if total < target:
        end = mid - 1
        # right search
    else:
        result = mid
        start = mid + 1
        
        
print(result)

#%%
# 정렬된 배열에서 특정 수의 개수 구하기.
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = list(map(int, input().split()))

def binary_search(a, target):
    if x not in a:
        return -1
    left_index = bisect_left(a, target)
    right_index = bisect_right(a, target)
    return right_index - left_index

print(binary_search(a, x))

#%%
# dongbin's
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    if x not in a:
        return -1
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

count = count_by_range(a, x, x)

if count == 0:
    print(-1)
    
else:
    print(count)
    

