from collections import deque

def bfs():
    global visited

    queue = deque()
    queue.append((0,0))
    visited[0][0] = matrix[0][0]
	
    while queue:
        row, col = queue.popleft()
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < R and 0 <= new_col < R:
                if visited[row][col] + matrix[new_row][new_col] < visited[new_row][new_col]:
                    visited[new_row][new_col] = visited[row][col] + matrix[new_row][new_col]
                    queue.append((new_row, new_col))
    return visited[-1][-1]

number = 0
INF = int(1e10)
drdc = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while True:
    R = int(input())
    if not R: break
    number += 1
    matrix = [list(map(int, input().split())) for _ in range(R)]
    visited = [[INF] * R for _ in range(R)]

    print(f'Problem {number}: {bfs()}')