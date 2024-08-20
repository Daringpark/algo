
'''
6 4
0100
1110
1000
0000
0111
0000

15
'''
# BOJ 2206 벽 뚫고 지나가기

from collections import deque

def bfs(start, f):


    if f:
        queue = deque([start])
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                new_row = row + dr
                new_col = col + dc
                # 범위 내
                if 0 <= new_row < N and 0 <= new_col < M:
                    # 값이 존재 하지 않을 때,
                    if not matrix[new_row][new_col]:
                        if visited[row][col] > visited[new_row][new_col]:
                            visited[new_row][new_col] = visited[row][col] + 1
                            queue.append((new_row, new_col))

    else:
        queue = deque([start])
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                new_row = row + dr
                new_col = col + dc
                # 범위 내
                if 0 <= new_row < N and 0 <= new_col < M:
                    # 값이 존재 하지 않을 때,
                    if not matrix[new_row][new_col]:
                        if visited[row][col] > visited[new_row][new_col]:
                            visited[new_row][new_col] = visited[row][col] + 1
                            queue.append((new_row, new_col))
                    else:
                        


N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    print(*matrix[i])
row, col = 0, 0
visited[row][col] = 1

bfs((row,col), 0)


if visited[N-1][M-1]:
    print(visited[N-1][M-1])
else:
    print(-1)