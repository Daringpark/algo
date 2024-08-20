# 14503 로봇 청소기
'''
N * M
# 0 0 (row, col) 제일 위 왼
# N-1, M-1 (row, col) 제일 아래 오

각 칸은 벽과 칸으로 이뤄져 있다.
청소기가 바라보는 방향이 존재하다.

1. 현재 칸이 청소 되지 않은 경우, 청소를 한다.

2. 현재 칸의 주변 4칸이 청소 되지 않은 빈칸이 없는 경우 (청소가 다 되어있는경우)
- 바라보는 방향을 유지하고, 후진 가능하다면 후진하여 1.
- 바라보는 방향의 뒤쪽 칸이 벽이라서 후진하지 못한다면, 작동 중지

3. 현재 칸의 주변 4칸이 청소되지 않은 빈칸이 있는 경우 (청소가 필요한 칸이 있는 경우)
- 반 시계로 90도 회전한다.
- 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 칸이면 한 칸 전진하고 1.
'''
import sys
sys.stdin = open("14503.txt")

drdc = [[-1,0], [0,1], [1,0], [0,-1]]
# 후진 하는 경우 direction + 2 % 4
# 회전하는 방향은 반 시계 direction + 3 % 4

def simulate():
    global Matrix
    row, col = startrow, startcol
    direction = startdir
    # 초반 세팅
    visited[row][col] = 1
    cnt = 1
    
    # simulation 시작
    while True:
        flag = 0 # 매 번 청소가 이뤄졌는지 안 이뤄졌는지 볼 것이다.

        # 우선 청소부터 해보자.
        # 현재 칸에서 탐색을 실행한다.
        for _ in range(4):
            # 청소를 진행하고 근처에 청소되지 않은 빈칸이 있는 경우 90도 회전
            # 0 > 3 > 2 > 1 > 0
            direction = (direction+3) % 4
            # 바라보는 방향
            new_row = row + drdc[direction][0]
            new_col = col + drdc[direction][1]
            if 0 <= new_row < N and 0 <= new_col < M:
                # 새로 가는 지점이 방문하지도 않았고, 빈 공간인 경우 발견.
                if not Matrix[new_row][new_col] and not visited[new_row][new_col]:
                    # 치워버려
                    cnt += 1
                    flag = 1
                    visited[new_row][new_col] = 1
                    # 방향 유지 및 움직이기
                    row = new_row
                    col = new_col
                    break
        
        # 청소 못했어? (해당 시행에서 청소했다면 건너 뛸 것이다.)
        if not flag:
            # 뒤로 후진해야한다... (direction은 유지)
            nd = (direction+2)%4
            new_row = row + drdc[nd][0]
            new_col = col + drdc[nd][1]
            # 후진 불가능
            if Matrix[new_row][new_col]:
                return cnt
            else: # 후진 가능 지역만 새롭게 row, col을 받는다.
                row = new_row
                col = new_col
        
N, M = map(int, input().split()) # matrix 전개
startrow, startcol, startdir = map(int, input().split()) # 시작 위치 + 보고 있는 방향
# 0 1 2 3 북 동 남 서 (시계 방향)
Matrix = [list(map(int, input().split())) for _ in range(N)]
# 0인 경우 무조건 청소되지 않은 칸이다.
# 1인 경우는 벽이다.
# 내가 지나갔던 1번을 다시 갈 필요가 없는가?
visited = [[0] * M for _ in range(N)] # 벽으로 만들어도 되는가?
print(simulate())