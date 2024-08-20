# 10810 공 넣기 브론즈 3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 100, 100 까지

space = [0]* (N+1) # 바구니 
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        space[n] = k

print(*space[1:])