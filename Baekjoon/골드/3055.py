
'''
5 4
.D.*
....
..X.
S.*.
....

4
'''
# BOJ 3055 탈출

# 시간제한 1초
# N*M = 2500
from collections import deque

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]
# 비버 굴은 D, 고슴도치는 S
# S가 D에 도달할 수 없다면, KAKTUS
# *은 물이고, X는 돌

flood_list = []
# 사전 구성하기
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '*':
            flood_list.append((i, j))
        elif matrix[i][j] == 'S':
            start = (i, j)
        elif matrix[i][j] == 'D':
            end = (i, j)

# 리스트로 저장하기 start를 처음 queue에서 빼기 + 홍수 진행시키기 [고슴도치 이동/물/고슴도치 이동/물 ...]
flood_list = [start] + flood_list
flood_q = deque(flood_list)
def bfs(end_row, end_col):

    while flood_q:
        row, col = flood_q.popleft()
        # queue 진행 이전에 확인하기
        if matrix[end_row][end_col] == 'S':
            return visited[end_row][end_col]
        
        # row, col이 일단 빠지게 되면, 해당 위치에서 4방향 탐색을 하게 됨
        # 그걸 이용해서 홍수를 구현할 수 있음
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            # 범위 안
            if 0 <= new_row < N and 0 <= new_col < M:
                
                # 조건 분기를 통해서 문제 해결
                if (matrix[new_row][new_col] == '.' or matrix[new_row][new_col] == 'D') and matrix[row][col] == 'S':
                # 현재 있는 칸이 시작 지점(matrix를 변화시켜주면서 고슴도치가 차지할 땅을 넓혀주자)
                    matrix[new_row][new_col] = 'S'
                    visited[new_row][new_col] = visited[row][col] + 1
                    flood_q.append((new_row, new_col))
                # 물 칸 확장하기
                elif (matrix[new_row][new_col] == '.' or matrix[new_row][new_col] == 'S') and matrix[row][col] == '*':
                    # 딛을 수 있는 칸이었거나, 고슴도치가 있을 땅
                    matrix[new_row][new_col] = '*'
                    flood_q.append((new_row, new_col))
    return "KAKTUS"

e_row, e_col = end
# 뒤에서부터 역행하자
print(bfs(e_row, e_col))


