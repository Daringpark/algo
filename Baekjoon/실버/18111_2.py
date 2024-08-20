
import sys
input = sys.stdin.readline

# M, N = 500 >> 25*1e4
M, N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

time = [0] * 257
height = 0
for i in range(257):
    blocks = B
    for row in matrix:
        for value in row:
            if value > i: # 더 높은 층이라면, 파야됨
                time[i] += 2 * (value - i)
                blocks += value - i
            else: # 더 낮은 층이라면 1초를 소모해서 블럭 추가
                time[i] += i - value
                blocks -= i - value

    if blocks >= 0 and time[i] <= time[height]:
        height = i # 시간을 더 적게 썼다면, 같았을 때도 더 높은 층으로 바꿔준다.
print(time[height], height)


# for i in range(M):
#     print(*matrix[i])

'''
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2

250 35
'''