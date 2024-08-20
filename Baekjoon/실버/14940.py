
# BOJ 14940 쉬운 최단거리 실버 1

from collections import deque
def bfs():

    queue = deque([(sr, sc)])

    while queue:
        row, col = queue.popleft()

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[row][col] + 1
                    queue.append((nr, nc))

N, M  = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 2:
            sr, sc = n, m
visited = [[0] * M for _ in range(N)]
bfs()

for n in range(N):
    for m in range(M):
        if matrix[n][m] == 1 and visited[n][m] == 0:
            visited[n][m] = -1

for row in visited:
    print(*row)

'''
3 4
2 1 1 1
1 0 1 1
0 1 0 1

0 1 2 0
1 0 3 0
0 0 0 0
'''