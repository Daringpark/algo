# 14501 퇴사

import sys
input = sys.stdin.readline
# N일 동안, N+1일째 되는 날에 퇴사하려고 한다.
# T = 걸리는 시간, P = 그것에 보수
# N은 최대 15일
# 만약, 1일에 3일 정도의 시간이 걸리다면, 4일부터 재상담이 가능하다.\

N = int(input())
days = [list(map(int, input().split())) for _ in range(N)]
DP = [0] * (N+1) # DP length N+1
max_value = 0
for i in range(N): # 돌아야 되긴 해
    for j in range(i+days[i][0], N+1): # 하나를 고르고 그 나머지 값들을 선택해야하기 때문에
        if DP[j] < DP[i]+days[i][1] : # 값어치를 비교할 것
            DP[j] = DP[i]+days[i][1]
# 완전 탐색이지만, 우리가 원하는 최대 값을 뽑아내는데에 memoization을 사용
# print(DP)
print(DP[-1]) # 끝까지 다 돌았을 때, N번째에 있는 값을 봐야함.