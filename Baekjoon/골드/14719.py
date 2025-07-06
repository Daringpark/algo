
# BOJ 14719 빗물 골드 5
# 구현, 풀어볼 만한 시뮬레이션 구현 문제

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
RAIN_MAP = list(map(int, input().split()))

answer = 0
for i in range(1, W-1): # want to search the max wall (left, right)
    left_max = max(RAIN_MAP[:i])
    right_max = max(RAIN_MAP[i+1:])

    edge_wall = min(left_max, right_max)

    if RAIN_MAP[i] < edge_wall: # compare with minimum wall height from highest wall of left, right
        answer += edge_wall - RAIN_MAP[i]

print(answer) 