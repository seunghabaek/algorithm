# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 03:18:08 2021

@author: seungha
"""

#%% - 입출력
# num 2588 (for문 사용)

# input 
a = int(input())
b = list(input())
n = len(b)
c = ''

# output
for i in range(n):
    c += b[i]
    print(a*int(b[n-i-1]))
    
print(a*int(c)) 


#%%
# num 10950

import sys
# input 
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)


#%%
# num 10951 (몇개인지 모르는 input 두개를 받는 경우)

import sys

while 1:
	try:                                                  # normal case
		a,b = map(int, sys.stdin.readline().split())
		print(a+b)
	except:                                               # error case
		break


#%%
# num 10952 (마지막 입력이 0 0 이 나오는 경우)

import sys

while 1:
	a,b = map(int, sys.stdin.readline().split())
	if a+b != 0:
		print(a+b)
	else:
		break


#%%
# num 10953 (하나의 숫자 + 그만큼의 input)

import sys

n = int(input())
for i in range(n):
	a,b = map(int, sys.stdin.readline().split(','))
	print(a+b)


#%%
# num 11021 (문자와 숫자가 공존 .format()사용)

import sys

n = int(input())

for i in range(n):
	a,b = map(int, sys.stdin.readline().split())
	print('Case #{}: {}'.format(i+1, a+b))


#%%
# num 11022 (더 많은 문자와 숫자)

import sys

n = int(input())

for i in range(n):
	a,b = map(int, sys.stdin.readline().split())
	print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))


#%%
# num 11718 (입력 받은 그대로 출력)  

while 1:
	try:
		a = str(input())       # sys.stdin.readline()을 쓰면 EOF를 빈 문자열로 return. 즉 필요없는 값이 return
		print(a)
	except:
		break	


#%%
# num 11719 (입력 받은 그대로 출력 - 공백, 빈칸 존재)

while 1:
	try:
		a = str(input())
		print(a)
	except:
		break


#%%
# num 11720 (입력 받은 숫자들의 합 구하기)

n = int(input())
a = list(str(input()))
list_sum = 0

for i in range(n):
	list_sum += int(a[i])

print(list_sum)


#%%
# num 11721 (입력받은 문자 10개씩 잘라서 출력)

a = str(input())

for i in range(0, len(a), 10):
	print(a[i:i+10])


#%%
# num 2741 (입력된 숫자까지 차례대로 출력)

n = int(input())

for i in range(1,n+1):
	print(i)


#%%
# num 2742 (입력된 숫자부터 역순으로 출력)

n = int(input())

for i in range(n, 0, -1):
	print(i)


#%%
# num 2739 (입력된 숫자를 구구단으로 만들기)

n = int(input())

for i in range(1, 10):
	print('{} * {} = {}'.format(n, i, n*i))

	
#%%
# num 1924 (2007년 달력) - dictionary 사용, runtime(type error) 해결

calendar = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

a, b = map(int,input().split())      # 반드시 두개 이상의 input에는 map을 해줄 것.(Type Error 방지)
c = 0

for i in range(1, a):
    c += calendar[i]
c += b

weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(weekday[c%7])


#%%
# num 8393 (n까지 합 구하기)

n = int(input())
a = 0

for i in range(1, n+1):
	a += i

print(a)


#%%
# num 10818 (숫자 입력받아서 최소값, 최대값 추출)

import sys
n = input()
a = list(map(int, sys.stdin.readline().split()))
print(min(a), max(a))


#%%
# num 2438 (주어진 입력만큼 *갯수 찍기)

n = int(input())   # 꼭 자료형 표기해줄 것.
a = str('')

for i in range(n):
	a += '*'
	print(a)


#%%
# num 2439 (주어진 입력만큼 *갯수 오른쪽정렬해서 찍기)

n = int(input())
a = str('')

for i in range(n):
	a += '*'
	print(a.rjust(n, ' '))	   # 오른쪽 정렬: rjust(), 왼쪽 정렬: ljust()


#%%
# num 2440 (주어진 입력만큼 *갯수 거꾸로 출력)

n = int(input()) 
a = str('*')

for i in range(n):
	print(a*(n-i))


#%%
# num 2441 (주어진 입력만큼 *갯수 거꾸로 오른쪽 정렬 출력)

n = int(input()) 
a = str('*')

for i in range(n):
	b = a*(n-i)
	print(b.rjust(n, ' '))


#%%
# num 2442 (주어진 입력*2 -1 개 만큼 * 출력(+2등차))

n = int(input())
a = str('*')

for i in range(n):
	b = a*(2*i+1)
	print(b.rjust(n+i, ' '))


#%%
# num 2445 (주어진 배열에서 규칙성 찾기)

n = int(input())
a = str('')

for i in range(1,2*n):
	if i <= n:
		b = (a*i).ljust(n, ' ')
		c = (a*i).rjust(n, ' ')
		print(b+c)
	else:
		b = (a*(2*n-i)).ljust(n, ' ')
		c = (a*(2*n-i)).rjust(n, ' ')
		print(b+c)


#%%
# num 2522 (주어진 배열에서 규칙성 찾기)

n = int(input())
a = str('*')

for i in range(n):
	if i <= n:
		b = (a*i).rjust(n, ' ')
		print(b)
	else:
		b = (a*(2*n-i)).rjust(n, ' ')
		print(b)


#%%
# num 2446 (주어진 배열에서 규칙성 찾기)

n = int(input())
a = str('*')
c = 2*n

for i in range(1, c):
    if i <= n:
        b = (a*(2*n-2*i+1)).rjust(c-i, ' ')
        print(b)
    else:
        b = (a*(2*i-2*n+1)).rjust(i, ' ')
        print(b)


#%%
# num 10991 (중간에 빈칸이 있는 * 입력 갯수만큼 출력)

n = int(input())
a = str('')

for i in range(n):
	a += '*'+' '
	print(a.rjust(n+i+1, ' '))


#%%
# num 10992 (*규칙 찾아서 풀기 [첫번째:1개, 마지막:2n-1개, 가운데:2개])

n = int(input())
a = str('')

for i in range(n):
	if i == 0:
		print(a.rjust(n+i, ' '))
	elif (i>0) & (i<n-1):
		b = a + (' ')*(2*i-1) + '*'
		print(b.rjust(n+i, ' '))
		b = ''
	else:
		c = a*(2*n-1)
		print(c)


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
# num 11053

# num 11055

# num 11722

# num 11054

# num 1912

# num 2579

# num 1699

# num 2133

# num 9461

# num 2225

# num 2011

# num 11052

#%%
# [이진 탐색]
# num 1654 (랜선 자르기) -> 시간복잡도에 대해서 더 공부..

def lan_cut(array, length):
	total = 0
	for x in array:
		total += (x//length)
	return total

k,n = map(int, input().split())
array = []
for i in range(k):
	array.append(int(input()))

start = 0
end = 2147483648

while True:
    mid = (start+end) // 2
    getlan = lan_cut(array, mid)
    
    if start >= end-1:
        break
    if getlan < n:
        end = mid
    else:
        start = mid

print(start)

#%%
# num 2805 (나무 자르기)
def cut_tree(array, length):
    total = 0
    for x in array:
        if x > length:
            total += (x - length)
    return total

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = 1000000000

while (start < end-1):
    mid = (start + end) // 2
    tree_length = cut_tree(array, mid)
    if tree_length < m:
        end = mid
    else:
        start = mid
print(start)

