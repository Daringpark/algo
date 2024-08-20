
# 백준 16236번 아기상어
from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(s_row, s_col):

    # 일반 BFS
    queue = deque()
    queue.append((s_row, s_col))
    visited = [[0] * N for _ in range(N)]
    visited[s_row][s_col] = 1

    prey = []
    while queue:

        row, col = queue.popleft()

        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                # 몸무게보다 작거나 같을 때 이동이 가능함
                if not visited[new_row][new_col] and weight >= matrix[new_row][new_col]:
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = visited[row][col] + 1

                # 값이 있으면서 먹을 수 있는(몸무게 미만의 크기 물고기)
                if matrix[new_row][new_col] and matrix[new_row][new_col] < weight:
                    dist_temp = visited[new_row][new_col]
                    if (dist_temp, new_row, new_col) not in prey:
                        prey.append((dist_temp, new_row, new_col))

    # row를 기준으로 그 다음 col을 기준으로 (제일 위, 제일 왼쪽 순서)
    if prey:
        prey.sort(key = lambda x: (x[0], x[1], x[2]))
    
    # 먹이 대기열이랑 위치 대기열 같이 return한다
    return prey

# 상어 위치 찾기
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 9:
            start_row, start_col = row, col
            # 변수에 저장과 함께 바로 위치 0으로 만들기
            matrix[row][col] = 0

# 상어 초기 몸무게는 2
weight = 2
weight_cnt = 0
result = 0

while True:

    prey_list = bfs(start_row, start_col)
    # 빈 리스트라면 (탐색을 진행했지만, 더 이상 먹이가 없을 경우)
    if not prey_list:
        break
    step, start_row, start_col = prey_list[0]
    result += step-1
    weight_cnt += 1
    matrix[start_row][start_col] = 0

    # 먹이를 먹고 크기가 커지는 경우
    if weight_cnt == weight:
        weight += 1
        weight_cnt = 0 # 초기화

print(result)