
# 11051 이항 계수 2

N, K = map(int, input().split())
mod = 10007

DP = [0] * (K+1) # 3 [0, 0, 0]
DP[0] = 1

for n in range(1, N+1):
    upper = min(n, K)
    # print(upper)
    for k in range(upper, 0 , -1):
        DP[k] = (DP[k] + DP[k-1])
    # print(DP)

print(DP[K] % mod)