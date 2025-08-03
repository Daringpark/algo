
# 6118 숨바꼭질
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

### Graph making
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

### BFS Logic
from collections import deque
queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    p = queue.popleft()

    for n_s in graph[p]:
        if not visited[n_s]:
            queue.append(n_s)
            visited[n_s] = visited[p] + 1

min_idx = 20000
dist = max(visited)
dist_count = 0

for idx in range(1, N+1):
    
    if visited[idx] == dist:
        min_idx = min(min_idx, idx)
        dist_count += 1

print(min_idx, dist-1, dist_count)