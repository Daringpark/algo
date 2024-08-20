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

    while queue:
        row, col = queue.popleft()

        cnt = 0
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if not matrix[new_row][new_col]:
                    cnt += 1
        visited[row][col] = 1 + cnt

        for dr, dc in drdc:
            new_row = row  + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if not visited[new_row][new_col] and matrix[new_row][new_col]:
                    # visited 처리를 안하는 이유는 어차피 popleft 이후에 visited 처리가 될 예정이기에
                    queue.append((new_row, new_col))

# 조각 세기
def bfs2(x, y):
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    while queue:
        row, col = queue.popleft()

        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if visited[new_row][new_col] and matrix[new_row][new_col]:
                    visited[new_row][new_col] = 0
                    queue.append((new_row, new_col))
    return 1

# 녹이기
def melt():
    for row in range(M):
        for col in range(N):
            if visited[row][col]:
                if matrix[row][col] + 1 - visited[row][col] > 0:
                    matrix[row][col] -= visited[row][col]
                    matrix[row][col] += 1
                else: # 음수 판별
                    matrix[row][col] = 0

# visited를 사용하지 않고 바로 처리를 해야한다?
# visted를 새로운 리스트로 정의





M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]

result = 0
while True:

    visited = [[0] * N for _ in range(M)]
    # 빙산
    for row in range(1, M):
        for col in range(1, N):
            if not visited[row][col]:
                bfs(row, col)

    # 근처의 물만큼 빙산 녹이기
    melt()

    # 빙산 조각 갯수 세기
    piece = 0
    for row in range(1, M):
        for col in range(1, N):
            if matrix[row][col] and visited[row][col]:
                piece += bfs2(row, col)
    
    if piece == 1:
        result += 1
    else:
        if piece == 0:
            print(0)
            exit()
        else:
            print(result+1)
            exit()