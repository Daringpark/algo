
# BOJ 14502 연구소 골드 4

import sys
from collections import deque
input = sys.stdin.readline

def combination(level, start, wall):
    global max_value

    # 기둥 3개를 뽑았을 경우
    if level == 3:
        # 최대 영역 수 - 기둥으로 들어갈 갯수 3개 미리 빼기
        result = total_space - 3

        # 임시로 벽 세우기
        for row, col in wall:
            matrix[row][col] = 1

        # 바이러스 퍼트리기 (퍼진 것 만큼)
        result -= bfs()
        
        # 바이러스 퍼진 결과가 더 크면
        if result > max_value:
            max_value = result

        # 벽 내리기
        for row, col in wall:
            matrix[row][col] = 0

        return

    # 재귀로 조합 뽑기
    for i in range(start, total_space):
        if not space_visited[i]:
            space_visited[i] = 1
            combination(level+1, i+1, wall + [space[i]])
            space_visited[i] = 0

def bfs():
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    cnt = 0
    for row, col in virus:
        queue.append((row, col))
        visited[row][col] = 1

    while queue:
        row, col = queue.popleft()
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < M:
                if not visited[new_row][new_col]:
                    if matrix[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = 1
                        cnt += 1

    return cnt

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]

# BFS 돌릴 용도
virus = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append((i,j))

# 기둥을 고를 용도
space = []
for i in range(N):
    for j in range(N):
        if not matrix[i][j]:
            space.append((i,j))
total_space = len(space)
space_visited = [0] * total_space

max_value = 0
combination(0, 0, [])
print(max_value)

'''
3 3
2 0 2
1 0 0
0 0 0
>> 3

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
 >> 9

0 0 0 0 1 0
1 0 0 1 0 2
1 1 1 0 0 2
0 0 0 1 0 2
 >> 9
17 - 8 = 9
(3+5)

17 -3 -5

'''