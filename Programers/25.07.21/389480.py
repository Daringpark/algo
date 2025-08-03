
# 코드챌린지 2차 예선 - 완전 범죄 (DP)


def solution(info, n, m):
    INF = float("inf")
    
    info_length = len(info)
    DP = [[INF] * m for _ in range(info_length + 1)]

    DP[0][0] = 0
    for i in range(1, info_length + 1):
        a, b = info[i-1][0], info[i-1][1]
        for j in range(m):
            DP[i][j] = min(DP[i][j], DP[i-1][j] + a)

            if j + b < m:
                DP[i][j+b] = min(DP[i][j+b], DP[i-1][j])
    min_value = INF
    for x in range(m):
        min_value = min(DP[info_length][x], min_value)
    
    if min_value >= n: result = -1
    else: result = min_value
    
    return result

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))