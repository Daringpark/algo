
from collections import deque

def BFS(start):
    global min_value, result

    visited = [0 for _ in range(N + 1)]
    queue = deque([start])
    visited[start] = 1

    while queue:
        item = queue.popleft()

        for next in graph[item]:
            if not visited[next]:
                visited[next] = visited[item] + 1
                queue.append(next)

    value = sum(visited)
    # 앞에서부터 보기 때문에 따로 처리 안해줘도 됨
    if min_value > value:
        min_value = value
        result = start

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# print(graph)
result = 0
min_value = int(1e5)

# 스타트 지점 i부터 BFS 탐색해보자.
for i in range(1, N+1):
    BFS(i)

print(result)