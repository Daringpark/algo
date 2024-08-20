
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]
x = []
y = []
for i in range(N):
    if 1 in Matrix[i]:
        x.append(i)
        for j in range(M):
            if Matrix[i][j] == 1:
                y.append(j)
res = (max(x)-min(x))+(max(y)-min(y))
print(res)