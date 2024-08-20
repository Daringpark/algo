
# 백준 2589 보물섬
from collections import deque

def bfs(start_row, start_col):

    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = 1
    max_cnt = 1

    while queue:
        row, col = queue.popleft()

        if max_cnt < visited[row][col]:
            max_cnt = visited[row][col]

        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if not visited[new_row][new_col] and matrix[new_row][new_col] == 'L':
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = visited[row][col] + 1

    return max_cnt

M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]

Land_list = []
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 'L':
            Land_list.append((i, j))

result = 0
for row, col in Land_list:
    visited = [[0] * N for _ in range(M)]
    max_value = bfs(row, col)
    if max_value > result:
        result = max_value

print(result-1)