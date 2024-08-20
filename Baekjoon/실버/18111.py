
import sys
input = sys.stdin.readline

def solve():
    global B

    min_value = 256
    max_value = 0
    for row in range(M):
        max_value = max(max_value, max(matrix[row]))
        min_value = min(min_value, min(matrix[row]))

    res_time = 1e12
    height = 0
    # 제거는 2초, 놓기는 1초
    for num in range(min_value, max_value+1):
        time = 0
        blocks = B
        for i in range(M):
            for j in range(N):
                    diff = matrix[i][j] - num
                    if diff > 0 :
                        blocks += diff
                        time += 2*diff
                    elif diff < 0:
                        blocks += diff
                        time += 1*(-diff)
        if blocks >= 0:
            if res_time > time:
                res_time = time
                height = num 

    return [res_time, height]

# M, N = 500 >> 25*1e4
M, N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
print(*solve())

# for i in range(M):
#     print(*matrix[i])

'''
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2

250 35
'''