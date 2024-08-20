

import sys
input = sys.stdin.readline

col, row = map(int, input().split())
N = int(input())
x, y = [0, col], [0, row]

for _ in range(N):

    dir, num = map(int, input().split())
    if dir: # 세로 자르기 (col)
        x.append(num)
    else:
        y.append(num)

result = 0
x.sort()
y.sort()
# 정렬과 완전탐색 이용
for i in range(len(x)-1):
    for j in range(len(y)-1):
        width = x[i+1] - x[i]
        height = y[j+1] - y[j]
        result = max(result, width*height)

print(result)