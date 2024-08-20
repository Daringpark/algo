
# BOJ 골드 5 A와 B 2
# DFS 풀이

import sys

S = list(input())
T = list(input())

def dfs(lst):
    if lst == S:
        print(1)
        sys.exit()
    
    # 답이 안나오게 된다면, 끝까지 뺐는데
    if len(lst) == 0:
        return 0
    
    if lst[-1]=='A': # T 끝 값이 A이면 제거 후 재귀
        dfs(lst[:-1])

    if lst[0] =='B': # T 시작이 B이면 제거 이후, 뒤집어서 재귀
        dfs(lst[1:][::-1])

dfs(T)
print(0)