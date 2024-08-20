
# 7:40
# BOJ 1012 유기농 배추 실버 2
from collections import deque

def bfs(start_row, start_col):

    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = 1

    # 100
    while queue:
        row, col = queue.popleft()
        
        # 2500 * 4
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < N and 0 <= new_col < M:
                if not visited[new_row][new_col] and matrix[new_row][new_col]:
                    visited[new_row][new_col] = 1
                    queue.append((new_row, new_col))

# T <= ?
T = int(input())
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(T):

    # M col, N row
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    # 2500
    cabbage_list = []
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
        cabbage_list.append((Y, X))


    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for cabbage in cabbage_list:
        x, y = cabbage
        if not visited[x][y]:
            bfs(x, y)
            cnt += 1

    print(cnt)