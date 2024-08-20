
# 1652 누울 자리를 찾아라

import sys
input = sys.stdin.readline

N = int(input())
matrix = [input() for _ in range(N)]
result_row = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[i][j] == '.':
            cnt += 1
        elif matrix[i][j] == 'X':
            if cnt >= 2:
                result_row += 1
            cnt = 0
        
        if j == N-1 and cnt >= 2:
            result_row += 1

result_col = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[j][i] == '.':
            cnt += 1
        elif matrix[j][i] == 'X':
            if cnt >= 2:
                result_col += 1
            cnt = 0
        
        if j == N-1 and cnt >= 2:
            result_col += 1

print(result_row, result_col)