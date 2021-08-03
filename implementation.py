# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:25:20 2021

@author: seungha
"""

# 상하좌우 문제

n = int(input())

x,y = 1,1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


# 이동계획 하나씩
for plan in plans:
    
    # 이동 후 좌표 구하기
    for i in range(len(plans)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동
        x,y = nx, ny
print(x, y)

#%%
# 시각 문제

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에서 3 확인 후 카운트
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

#%%
# 왕실의 나이트 문제 - 2차원 리스트 

input_data = input()
row = int(input_data[1])
# ascii code 변환
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 움직일 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동 가능한지 판단
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

#%%
# 문자열 재정렬

data = input()
result = []
value = 0

# 문자 하나씩 확인
for x in data:
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
        
result.sort()

if result != 0:
    result.append(str(value))

print(''.join(result))


        