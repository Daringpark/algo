
def left_rotate(number, dir):

    # 입력이 0 미만일 수 있다. (idxERR)
    if number < 0:
        return
    
    # 돌리기 전꺼랑 돌릴거랑 비교 (한 방향 왼쪽 비교)
    if gears[number][2] != gears[number+1][6]:
        left_rotate(number-1, -dir)
        gears[number].rotate(dir)

def right_rotate(number, dir):
    # 입력이 3 초과일 수 있다. (idxERR)
    if number > 3:
        return
    
    # 돌리기 전꺼랑 돌릴거랑 비교
    if gears[number-1][2] != gears[number][6]:
        # 다음 꺼는 반대로 돌려야 됨
        right_rotate(number+1, -dir)
        gears[number].rotate(dir)

from collections import deque
# 0, 1, 2, 3
gears = [deque(list(map(int, input()))) for _ in range(4)]
# [0] 1 [[2]] 3 [4] 5 [[6]] 7
N = int(input())

for _ in range(N):
    # 기어 넘버, direction(방향)
    gn, dr = map(int, input().split())

    # 지금 톱니에서 왼쪽과 오른쪽을 나눠서 반대 방향으로 돌려볼 준비
    left_rotate(gn-2, -dr)
    right_rotate(gn, -dr)
    # 확실히 본인것도 돌려줘야 함 (본인 방향으로)
    gears[gn-1].rotate(dr)

result = 0
for i in range(4):
    if gears[i][0]%2:
        result += 2**i

print(result)