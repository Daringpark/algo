'''
5 5 1
1 4
1 2
2 3
2 4
3 4

'''

# stack DFS
import sys
input = sys.stdin.readline
from collections import deque

def dfs(node):
    stack = deque()
    stack.append(node)
    cnt = 1
    while stack:
        item = stack.pop()
        # 방문 처리를 먼저 한다
        if not visited[item]:
            visited[item] = cnt
            cnt += 1

        # 추가로 stack에 넣어주기
        for new_s in graph[item]:
            if not visited[new_s]:
                stack.append(new_s)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

dfs(R)
for node in range(1, N+1):
    print(visited[node])