# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:36:55 2021

@author: seungha
"""
#%%
# 11047 - coin idea: sort(reverse=True)
n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
coin_list.sort(reverse=True)

cnt = 0
for coin in coin_list:
    cnt += k // coin
    k %= coin
print(cnt) 
       

#%%
# 2875 - team building
n,m,k = map(int, input().split())
cnt = 0
while n*m >=0 and n+m >= k:
    n -= 2
    m -= 1
    cnt += 1
print(cnt-1)

#%%
# 10610 - 약수의 정의 활용
n = list(map(int,input()))
n.sort(reverse=True)

result = ''
if (0 in n) and (sum(n) % 3 ==0):
    for i in n:
        result += str(i)
    print(result)
else:
    print(-1)
    
#%%
# 1783


#%%
# 1931

n = int(input())
room = []
for i in range(n):
    room.append(list(map(int,input().split())))
room = sorted(room, key=lambda x:(x[1], x[0]))  

cnt = 1
i = 1
start = room[0][0]
end = room[0][1]

while i < n:
    if room[i][0] >= end:
        end = room[i][1]
        cnt += 1
        i += 1
    else:
        i += 1
print(cnt)


#%%
# 11399

n = int(input())
time = list(map(int, input().split()))
time.sort()

dp = [0] * (n+1)
dp[0] = time[0]
for i in range(1, n):
    dp[i] = dp[i-1] + time[i]
print(sum(dp))

#%%
# 2873


#%%
# 1744

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

a = []
b = []
c = []
if n % 2 == 0:
# 위에서부터
    for i in range(n-1, -1, -2):
        if num[i] * num[i-1]  >0
        a.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    up = sum(a)
# 아래에서부터
    for i in range(0, n, 2):
        b.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    down = sum(b)
# 위 아래에서
    mid = n//2
    for i in range(0, mid, 2):
        c.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    for i in range(n-1, mid, -2):
        c.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    up_down = sum(c)
else:
# 위에서부터
    for i in range(n-1, -1, -2):
        a.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    up = sum(a)+num[0]
# 아래에서부터
    for i in range(0, n, 2):
        b.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    down = sum(b)+num[n-1]
# 위 아래에서
    mid = n//2
    for i in range(0, mid, 2):
        c.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    for i in range(n-1, mid, -2):
        c.append(max(num[i] + num[i-1], num[i]*num[i-1]))
    up_down = sum(c)+num[mid]    
print(max(up, down, up_down))