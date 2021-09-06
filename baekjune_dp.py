# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 01:05:12 2021

@author: seungha
"""
#%%
# [dynamic programming]
# num 1463 (1 만들기-3,2로 나누기,-1)

n = int(input())
dp = [0]*(n+1)

dp[1] = 0

for i in range(2, n+1):
	dp[i] = dp[i-1]+!
	if i % 6 == 0:
		dp[i] = min(dp[i], dp[i//3]+1, dp[i//2]+1)
	elif i % 3 == 0:
		dp[i] = min(dp[i], dp[i//3]+1)
	elif i % 2 == 0:
		dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])

#%%
# num 11726 - 2xn 도형을 1x2, 2x1 도형으로 채우기

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] =2
    elif i >= 3:
        dp[i] = dp[i-1] + dp[i-2]
        
print(dp[n]%10007)

#%%
# num 11727 - 2xn 2

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i ==2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + 2*dp[i-2]
        
print(dp[n]%10007)

#%%
# num 9095 - 1,2,3으로 숫자 만들기

def fibo_3(alpha):
    dp = [0] * (alpha+1)
    for j in range(1, alpha+1):
        if j == 1:
            dp[j] = 1
        elif j == 2:
            dp[j] = 2
        elif j == 3:
            dp[j] = 4
        else:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    return dp[alpha]

n = int(input())
a = list(int(input()) for i in range(n))

for i in range(n):
    print(fibo_3(a[i]))

#%%
# num 10844 - 계단 수 구하기

n = int(input())
dp = [[0]*10 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(10):
        if (i == 1 and j >= 1):
            dp[i][j] = 1
        elif i >= 2:
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

print((sum(dp[n]))%1000000000)

#%%
# num 11057 - 오르막 수 구하기

n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 미리 define 해주는게 빠름.

for i in range(2, n+1):
    for j in range(0, 10):
        dp[i][j] = sum(dp[i-1][0:j+1]) # list slicing

print(sum(dp[n])%10007)

#%%
# num 2193 - pinary number(특수한 이진수)

n = int(input())
dp = [1] * (n+1) # dp[1], dp[2] 둘다 1이라서 가능.

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])

#%%
# num 9466


#%%
# num 2156 - 1로 만들기 복습.

import sys

n = int(input())
p = list(int(sys.stdin.readline()) for _ in range(n))
dp = [0] * (n+1)

if n == 1: # index setting
    print(p[0])
else:
    dp[1], dp[2] = p[0], p[0] + p[1]
    
    for i in range(3, n+1):
        dp[i] = dp[i-2] + p[i-1]
        dp[i] = max(dp[i], dp[i-1], dp[i-3] + p[i-2] + p[i-1])
    
    print(dp[n])


#%%
# num 11053 - 가장 크게 증가하는 부분 수열 : 앞에서부터 차례대로 판단.
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(n):
    if i == 0:
        dp[i] = 1
    else:
        for j in range(i):
            if (a[i] > a[j]) and (dp[i] < dp[j]):
                dp[i] = dp[j]
        dp[i] += 1

print(max(dp))
#%%
# num 11055 - 가장 긴 증가하는 수열(합 포)
n = int(input())
a = list(map(int, input().split()))

dp = list(x for x in a)

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])   # 계속 전 값과 비교.

print(max(dp))



#%%
# num 11722 = 가장 긴 감소하는 수열
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(n):
    for j in range(i):
        if (a[i] < a[j]) and (dp[i] < dp[j]):
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

#%%
# num 11054 - 가장 큰 바이토닉 수열
n = int(input())
a = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n+1)]

for i in range(len(a)):
    for j in range(i):
        if (a[i] > a[j]) and (dp[i][0] < dp[j][0]):
            dp[i][0] = dp[j][0]
    dp[i][0] += 1

for k in range(len(a)-1, -1, -1):
    for l in range(len(a)-1, k-1, -1):
        if (a[k] > a[l]) and (dp[k][1] < dp[l][1]):
            dp[k][1] = dp[l][1]
    dp[k][1] += 1

result = [dp[i][0] + dp[i][1] for i in range(len(a))]
print(max(result)-1)

#%%
# num 1912 - 연속된 수의 합의 최댓값
n = int(input())
a = list(map(int, input().split()))

dp = []

for i in range(len(a)):
    if i == 0:
        dp.append(a[i])
    else:
        dp.append(max(a[i],  a[i]+a[i-1], a[i]+dp[i-1]))
print(max(dp))

#%%
# num 2579
n = int(input())
a = list(int(input()) for i in range(n))

dp = [0] * (n+1)

for i in range(n):
    if i == 0:
        dp[i] = a[i]
    if i == 1:
        dp[i] = a[i] + dp[i-1]
    elif i == 2:
        dp[i] = a[i] + max(a[i-1], dp[i-2])
    elif i >= 3:
        dp[i] = a[i] + max(a[i-1] + dp[i-3], dp[i-2]) # 항상 겹치는 것이 있을지 확인. 
print(dp[n-1])
#%%
# num 1699


#%%
# num 2133

#%%
# num 9461

def fibo(n):
    dp = [0] * (n+1)
    if n < 4:
        dp[n] = 1
    elif n >= 4:
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4, n+1):
            dp[i] = dp[i-2] + dp[i-3]
    return dp[n]

n = int(input())
result = [int(input()) for _ in range(n)]

for a in result:
    print(fibo(a))

#%%
# num 2225

#%%
# num 2011

#%%
# num 11052
n = int(input())
a = list(map(int, input().split()))

