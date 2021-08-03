# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 02:32:50 2021

@author: seungha
"""
#%% 
# 거스름 돈 거슬러 주기

n = 1260
Count = 0

array = [500, 100, 50, 10]

for coin in array:
    Count += n // coin
    n %= coin
print(Count)


#%%
# 1만들기 - dynamic programming

n = 25
k = 3

dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % k == 0:
        dp[i] = min(d[i], dp[i//k] + 1)
    
print(dp[n])

#%%
# 1만들기 - greedy

n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기.
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수(n<k)에 대하여 1씩 빼기 -> 2 or 1만 남기 때문
result += (n-1)
print(result)

# -> 반복문 하나에 다 들어있으므로 반복문의 횟수가 적어짐. -> log 시간 복잡

#%%
# 곱하기 혹은 더하기
# mine

data = input()
result = int(data[0])

for i in range(1, len(data)):
    result = max(result*int(data[i]), result+int(data[i]))
    
print(result)

# dongbin's

data = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)

#%%
# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
# 그룹 인원 수
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

    