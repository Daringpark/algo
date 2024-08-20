'''
4 6
101111
101010
101011
111011

'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        row, col = queue.popleft()
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < M:
                if not visited[new_row][new_col]:
                    if matrix[new_row][new_col]:
                        visited[new_row][new_col] = visited[row][col] + 1
                        queue.append((new_row, new_col))
        
N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

bfs((0,0))
print(visited[N-1][M-1])