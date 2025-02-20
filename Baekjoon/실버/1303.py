
from collections import deque

N, M = map(int, input().split())
matrix = list(list(input()) for _ in range(M))
visited = [[0] * N for _ in range(M)]
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

total_white = 0
total_black = 0

def matrix_calculate():
    global visited, total_black, total_white
    queue = deque()
    
    for i in range(M):
        for j in range(N):

            if matrix[i][j] == 'B':
                flag = False
                black_score = 0
            else:
                flag = True
                white_score = 0

            # BFS
            if not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1
                if flag: white_score += 1
                else: black_score += 1
            
            while queue:
                row, col = queue.popleft()

                for dr, dc in drdc:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < M and 0 <= new_col < N:
                        # W
                        if not visited[new_row][new_col]:
                            if flag and matrix[ new_row][new_col] == 'W':
                                white_score += 1
                                visited[new_row][new_col] = 1
                                queue.append((new_row, new_col))
                            elif not flag and matrix[new_row][new_col] == 'B':
                                black_score += 1
                                visited[new_row][new_col] = 1
                                queue.append((new_row, new_col))

            if flag: total_white += white_score**2
            else: total_black += black_score**2

matrix_calculate()
print(total_white, total_black)