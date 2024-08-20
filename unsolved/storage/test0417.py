# 일직선으로 앞, 뒤, 옆, 대각선 어떤 방향이든 원하는 만큼 이동할 수 있음

# 두가지 방법
# 좌표 N개를 미리 뽑고 check할것이냐
# 1개씩 뽑아가면 check할것이냐

# import sys
# input = sys.stdin.readline
# N x N 체스판

# 퀸들이 서로 공격 못하도록
# 서로다른 대각선 가로 세로 가지도록

import time

start_time = time.time()
# row, 예비 col, 지금까지 만들어진 N-queen 배치 리스트
def check(k,i, lst):
    # 지금까지 만들어진 길이 [0, 1] = 2
    n = len(lst)

    # row, col을 리스트에서 빼낸다.
    for r,c in lst:
        # 세로 직선 확인
        # 리스트에 있는 컬럼들이랑 예비 컬럼이랑 같을 때, False
        if i == c:
            return False

        # 대각선 확인
        # \ 방향 확인
        left_i = i + -1*n # 왼쪽 방향 내려가기
        # 리스트에 있는 컬럼이랑 만들어진 컬럼이랑 비교함
        if left_i == c:
            return False

        right_i = i + 1*n # 오른쪽 방향 내려가기
        # 리스트에 있는 컬럼이랑 만들어진 컬럼이랑 비교함
        if right_i == c:
            return False
        # 위로 올라오는거네
        n -= 1

    return True

N = int(input())
cnt = 0
lst = []
def chess(k, lst):
    global cnt

    if k == N:
        cnt += 1
        return

    # 후보 col = i
    for i in range(N):
        # row, col, lst가 붙음
        if check(k,i, lst):
            # row + 1, 지금 만들어진 리스트에 현재 (row, col) extend
            chess(k+1, lst+[(k,i)])
    return

chess(0, [])
print(cnt)
end_time = time.time()
exceution_time = end_time - start_time

print(exceution_time)