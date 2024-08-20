from collections import deque

# N의 개수가 50, M 또한 N보다 작거나 같음
# NM = 25 1e2
N, M = map(int, input().split())
pick = list(map(int, input().split()))
numbers = deque(range(1, N+1))
# 왼쪽으로 돌리거나 오른쪽으로 돌릴 때, 카운팅 해 줄 예정
n = N
cnt = 0
for p in pick:
    a = numbers.index(p)
    b = n - a
    if a >= b:
        numbers.rotate(b)
        cnt += b
    else:
        numbers.rotate(-a)
        cnt += a
    numbers.popleft()
    n -= 1
print(cnt)

# numbers.rotate(-1)
# # 왼쪽 회전
# numbers.rotate(1)
# # 오른쪽 회전