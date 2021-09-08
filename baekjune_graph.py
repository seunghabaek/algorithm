# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:23:23 2021

@author: seungha
"""
#%%
# 1260 - dfs, bfs print both of them
from collections import deque


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 0
    while(queue):
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)

#%%
# 11724

#%%
# 1707

#%%
# 10451

#%%
# 2331

#%%
# 9466

#%%
# 2667

#%%
# 4963

#%%
# 7576

#%%
# 2178

#%%
# 2146

#%%
# 1991

#%%
# 1725

#%%
# 1167

#%%
# 1967
