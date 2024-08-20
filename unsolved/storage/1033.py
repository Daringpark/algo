
# 1033 칵테일 정수론 

N = int(input())
# [x] * N

for i in range(N-1):
    a, b, p, q = map(int, input().split())
    # 4 0 1 1
    # 4번째와 0번째의 비율은 1:1
    # 4 1 3 1
    # 4번재와 1번째의 비율은 3:1
    # 이 합이 제일 작아야함.