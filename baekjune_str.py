# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:18:21 2021

@author: seungha
"""

#%%
# 7575

#%%
# 1230 - java to cpp
b = input()
a = list(b) # 나눠서 받기
j = []
c = []
answer = ''

if b.lower() != b: # java
    for x in a:
        if (x >='A') and (x<='Z'):
               j.append(a.index(x))
    for y in j:
        a.insert(y, '_') 
        a[y] = a[y].lower()

elif b.lower() == b: # cpp
    for x in a:
        if x == '_':
            c.append(a.index(x))
            a.remove('_')
    for y in c:
        a[y] = a[y].upper()
    a[0].lower()
else:
    print("Error")

for i in a:
    answer += i
print(answer)

# 다른 방법

b = input()
a = list(b) # 나눠서 받기

j = []
c = []
answer = ''

if b.lower() != b: # java to cpp
    for x in a:
        if (x >= 'A') and (x <= 'Z'):
            j.append('_')
            j.append(x.lower())
        else:
            j.append(x)
    
    for i in j:
        answer += i
    print(answer)

elif b.lower() == b: # cpp to java
    for x in range(len(a)):
        if a[x] == '_':
            a[x+1] = a[x+1].upper()
        else:
            c.append(a[x])

    for i in c:
        answer += i
    print(answer)

elif a[0] ='_' or a[-1] = '_'
    print("Error")





#%%
# 9251

#%%
# 9252

#%%
# 1958

#%%
# 5582

#%%
# 9249

#%%
# 1032

#%%
# 1543

#%%
# 1759

#%%
# 1919

#%%
# 1213

#%%
# 2079

#%%
# 3613

#%%
# 9996

#%%
# 2135

#%%
# 3033

#%%
# 8913

#%%
# 3080

#%%
# 9250

#%%
# 1701

#%%
# 9248

#%%
# 1605