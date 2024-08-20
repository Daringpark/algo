
# BOJ 14890 경사로 골드 3

import time
start_time = time.time()
def check(lst):

    # 한 리스트를 기준으로 왼쪽 -> 오른쪽, 오른쪽 -> 왼쪽까지 초기화 된 visited를 가지고 두 방향 동시에 본다.
    # 겹치는 path가 생겨도 상관없다. # 경사로가 대각선 방향으로 세워지는 경우는 케이스에 없었다.
    # 기준점을 뭐로 둘까? 높은거? 낮은거? 높은 것을 기준으로 두자. 높은 것에서 내려가는 식으로 구해보자.
    # 왼쪽부터 오른쪽으로 탐색 (열의 경우 위에서부터 아래로)

    visited = [0] * N
    for i in range(N-1): # 시작 지점 설정
        if lst[i] - lst[i+1] == 1: # 높이 차이 확인 완료
            flat_height = lst[i+1]
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if lst[j] != flat_height:
                        return 0
                    elif visited[j]:
                        return 0
                    visited[j] = 1
                else:
                    return 0

        elif lst[i] == lst[i+1]: # 높이 차이가 없어요! >> 연속되게 높이 차이가 안나야된다.
            continue

        elif abs(lst[i]-lst[i+1]) > 1: # 이건 곧 죽어도 경사로를 설치 못해요!!
            return 0

    # 오른쪽부터 왼쪽으로 탐색 (열의 경우 아래서부터 위로)
    for i in range(N-1, 0, -1):
        if lst[i] - lst[i-1] == 1:
            flat_height = lst[i-1]
            for j in range(i-1, i-L-1, -1):
                if 0 <= j < N:
                    if lst[j] != flat_height:
                        return 0
                    elif visited[j]:
                        return 0
                    visited[j] = 1
                else:
                    return 0

        elif lst[i] == lst[i-1]:
            continue

        elif abs(lst[i]-lst[i-1]) > 1:
            return 0

    return 1

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 경사로를 확인할 때 양쪽을 확인해야한다.
result = 0

# 행을 기준으로 탐색
for row in range(N): # 0 ~ N-1
    # 길을 생성 가능하다 = 1; else 0
    if check(matrix[row]):
        result += 1

# 열을 기준으로 탐색
for col in range(N):
    # 길을 생성 가능하다 = 1; else 0
     if check([matrix[row][col] for row in range(N)]):
        result += 1

# 최대 값은 2N (높이가 일정해서 아예 놓지 않은 경우로 행 탐색으로 N과 열 탐색으로 N개 나올 경우)
print(result)
# 디버깅용
# print(result_row, result_col)

# print(time.time() - start_time)