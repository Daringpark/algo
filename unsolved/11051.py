from itertools import combinations as cb

N, K = map(int, input().split())
res = len(set(cb(range(N), K)))
print(res%10007)

# 메모리 초과


# DP로 풀이