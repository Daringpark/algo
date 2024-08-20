'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        row, col = queue.popleft()

        cnt = 0
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                # visited -1 해줘야 근처 물 수
                if not matrix[new_row][new_col]:
                    visited[row][col] += 1

                if not visited[new_row][new_col] and matrix[new_row][new_col]:
                    visited[new_row][new_col] = 1
                    queue.append((new_row, new_col))


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]

result = 0
while True:

    visited = [[0] * N for _ in range(M)]
    # 빙산
    piece = 0
    for row in range(1, M):
        for col in range(1, N):
            if not visited[row][col] and matrix[row][col]:
            # 이어지는 것까지 확인해서 piece 개수 세기
                bfs(row, col)
                piece += 1

    for row in range(1, M):
        for col in range(1, N):
            if visited[row][col]:
                matrix[row][col] -= visited[row][col]
                matrix[row][col] += 1
            if matrix[row][col] < 0:
                matrix[row][col] = 0
    
    # 첫 번째 깎였을 때, 
    if piece == 1:
        result += 1
    else:
        if piece == 0:
            print(0)
            exit()
        else:
            print(result)
            exit()