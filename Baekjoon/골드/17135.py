
# BOJ 17135 캐슬 디펜스 골드 3

import sys
input = sys.stdin.readline
from collections import deque

# 2. 조합으로 archer의 위치를 뽑아두기
def make_combi(level, start, lst):
    
    if level == 3:
        archer_position_list.append(lst)
        return

    for i in range(start, M):
        if not visited[i]:
            visited[i] = 1
            make_combi(level+1, i+1, lst+[i])
            visited[i] = 0

# 3. 아처의 위치에서 적에게 화살 쏴 matrix 변화시키기
def kill(archer_position):
    new_matrix = [row[:] for row in matrix]
    kill_visited = [[0] * M for _ in range(N)]

    death_cnt = 0

    # 궁수들 바로 위에 있는 값
    for i in range(N-1, -1, -1):
        # 위로 올라가면서 스텝을 옮김 (1, 2, 3, ...)
        # 죽일 녀석들을 담을 배열
        current_step = []

        # 3개가 들어 있는 배열에서 아처를 하나씩 꺼내준다.
        for archer_col in archer_position:
            # 바로 위에 있는 타일만 1의 길이를 가지고 있음
            queue = deque([(i, archer_col, 1)])

            while queue:
                row, col, dist = queue.popleft()

                # 적을 찾은거니까
                if new_matrix[row][col] == 1:
                    current_step.append((row, col))
                    if not kill_visited[row][col]:
                        kill_visited[row][col] = 1
                        death_cnt += 1
                    # 찾아서 죽였기에, 계속 탐색하면 안됨
                    break
                    
                # 잡을 수 있는 곳을 다시 탐색해보자
                if dist < D:
                    # 좌 상 우
                    for dr, dc in [(0, -1), (-1, 0), (0, 1)]:
                        # queue에서 뽑은 값은 최대 D까지
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < N and 0 <= new_col < M:
                            queue.append((new_row, new_col, dist+1))

        for row, col in current_step:
            new_matrix[row][col] = 0
    return death_cnt

# 1. 데이터 불러오기
N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 모든 조합에서 궁수가 적을 죽일 수 있는 최대 값을 출력해야한다.
archer_position_list = deque()
visited = [0 for _ in range(M)]
make_combi(0, 0, [])

# 5. 마지막 출력
result = 0
for pos in archer_position_list:
    # max값을 뽑아야 하기에, result랑 죽여서 나온 death_cnt를 비교한다.
    result = max(result, kill(pos))
print(result)