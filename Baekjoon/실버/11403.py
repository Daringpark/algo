from collections import deque

N = int(input())

# Graph making
graph = [[] for _ in range(N+1)]
for i in range(N):
    end_points = list(map(int, input().split())) 
    for j in range(N):
        if end_points[j] == 1:
            graph[i+1].append(j+1)

visited = [[0] * N for _ in range(N)]

for s in range(N):
    queue = deque()
    for n in graph[s+1]:
        queue.append((s, n-1))
    
    while queue:
        start, node = queue.popleft()

        if not visited[s][node]:
            visited[s][node] = 1
            for next_node in graph[node+1]:
                queue.append((node, next_node-1))

for i in range(N):
    print(*visited[i])