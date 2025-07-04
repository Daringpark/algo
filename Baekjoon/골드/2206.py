
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

def bfs(start):
    global visited

    queue = deque([start])
    while queue:
        row, col, flag = queue.popleft()

        if row == N-1 and col == M-1:
            return visited[row][col][flag]

        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
            new_row = row + dr
            new_col = col + dc
            # 범위 내
            if 0 <= new_row < N and 0 <= new_col < M:
                # 다음 이동지가 벽이 있고, 벽 파괴를 사용하지 않은 경우
                if matrix[new_row][new_col] == 1 and flag == 0:
                    visited[new_row][new_col][1] = visited[row][col][0] + 1
                    queue.append((new_row, new_col, 1)) # 벽 파괴를 사용
                # 일반적으로 이동하는 경우 (공간이 있고 방문하지 않은 칸)
                elif matrix[new_row][new_col] == 0 and visited[new_row][new_col][flag] == 0:
                    visited[new_row][new_col][flag] = visited[row][col][flag] + 1
                    queue.append((new_row, new_col, flag))

    return -1

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     print(*matrix[i])
str_row, str_col = 0, 0
visited[str_row][str_col][0] = 1

print(bfs((str_row, str_col, 0)))
# for i in range(N):
#     print(*visited[i])