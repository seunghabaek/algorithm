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

#%%
# DFS 예제
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# graph 초기화
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]    # 각 노드에 연결된 노드를 리스트로 초기화

# 각 노드가 방문된 정보를 초기화
visited = [False] * 9

dfs(graph, 1, visited)
    
#%%
# BFS ex
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='') # 줄바꿈 원치 않는 출력
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    ]

visited = [False] * 9

bfs(graph, 1, visited)

#%%
# 음료수 얼려먹기 문제
def dfs(x, y):
    # range inspection
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우 방문처리
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# input
n, m = map(int, input().split())

# 2차원 리스트
graph = []
for i in range(n):
    graph.append(list(map(int,input)))
    
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 실행
        if dfs(i, j) == True:
            result += 1
    
print(result)
        
#%%
# 미로 탈출 문제
from collections import deque

# N, M 가져옴
n, m = map(int, input().split())

# 지도 가져옴
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네가지 방향 초기화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 범위
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시(괴물)
            if graph[x][y] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] == graph[x][y] + 1
                queue.append(nx, ny)
# 가장 오른쪽 아래까지의 최단 거리 반환
return graph[n - 1][m - 1]