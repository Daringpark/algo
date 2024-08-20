from collections import deque
 
N = int(input())
max_value = 0
graph = []
for row in range(N):
    graph.append(list(map(int, input().split())))
    for col in range(N):
        if graph[row][col] > max_value:
            max_value = graph[row][col] 

drdc = [(-1,0), (0,1), (1,0), (0,-1)]
def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        row, col = q.popleft()
        
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                if graph[new_row][new_col] > value and visited[new_row][new_col] == 0:
                    visited[new_row][new_col] = 1
                    q.append((new_row, new_col))

result = 0
for k in range(max_value): 
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(N):
            if graph[row][col] > k and not visited[row][col]: 
                bfs(row, col, k, visited)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)