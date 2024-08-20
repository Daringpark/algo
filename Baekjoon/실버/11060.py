'''
10
1 2 0 1 3 2 1 5 4 2
'''
# 초기 풀이

import sys
sys.stdin = open('11060_input.txt')
def make_graph(): # dictionary로 만들어야할듯
    global graph
    for i in range(N): # 0 ~ 9 까지 확인하기
        amount = maze[i]
        graph[i+1] = deque()
        for j in range(1, amount+1):
            graph[i+1].append((i+1+j))

from collections import deque
def BFS(start):
    # 그려진 그래프에서 Queue를 활용한 BFS를 한다.
    line = deque([start])
    level_dict[start] = 0
    while line:
        item = line.popleft()
        if graph[item]:
            for w in graph[item]:
                line.append(w)
                level_dict.setdefault(w, 0)
                if not level_dict[w]:
                    level_dict[w] = level_dict[item] + 1
                if w >= N:
                    return level_dict[w]
    if start >= N:
        return  level_dict[start]
    else : return -1

N = int(int(input()))
maze = deque(map(int, input().split()))
graph = dict()
level_dict = dict()
make_graph()
print(BFS(1))

