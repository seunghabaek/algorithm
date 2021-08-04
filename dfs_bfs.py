# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:13:03 2021

@author: seungha
"""
#%%
# stack example - 파이썬의 리스트가 동작하는 방식과 동일.

stack = []

# insert(5) -> insert(2) -> insert(3) -> insert(7) -> delete() -> insert(1) -> insert(4) -> delete()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# delete 연산
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
print(stack)

#%%
# queue example

from collections import deque

queue = deque()

# insert(5) -> insert(2) -> insert(3) -> insert(7) -> delete() -> insert(1) -> insert(4) -> delete()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#%%
# 재귀 함수
def recursive_function(i):
	if i == 100:
		return
	print('{}번쨰 재귀함수에서 {}번째 재귀함수를 호출합니다.'.format(i, i+1))
	recursive_function(i+1)
	print('{}번째 재귀함수를 종료합니다.'.format(i))
recursive_function(1)

#%%
# factorial

# 반복문으로 구현할때
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례데로 곱하기
    for i in range(1,n+1):
        result *= i
    return result

# 재귀 함수로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)!을 그대로 구현
    return n * factorial_recursive(n-1)

#%%
# 유클리드 호재법
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return(b, a % b)
    
print(gcd(192, 162))