# 가로 세로 최대 100
import sys
input = sys.stdin.readline
from collections import deque

def bfs():

    q = deque() # 공기에 접촉한 부분을 넣기 위해서
    melt_cheese = deque()
    q.append([1,1])

    while q:
        row, col = q.popleft()
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = 1
                    if matrix[new_row][new_col]: # 치즈면
                        melt_cheese.append([new_row, new_col]) # 따로 넣어서 한번에 녹이기
                    else:
                        q.append([new_row, new_col])
                        
    for row, col in melt_cheese:
        matrix[row][col] = 0
        
    return len(melt_cheese) # 녹인 치즈 개수를 반환

drdc = [[-1,0], [0,1], [1,0], [0,-1]]
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
cheese = 0 # 전체 치즈수를 계산해 냄
for i in range(1, M-1):
    # 전체 메트릭스를 순회하면서 1을 뽑아내야함.
    cheese += sum(matrix[i]) # 한 줄에 있는 치즈 개수를 확 계산

time = 1 # 첫 시작이 1이 시작, while을 돌게 되는 순간 time은 1
while True:
    visited = [[0] * N for _ in range(M)] # 계속 갱신
    melted_cheese = bfs()
    cheese -= melted_cheese
    if cheese == 0: # 목표에 도달
        print(time, melted_cheese, sep='\n')
        break
    time += 1