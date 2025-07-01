

# 백준 17619 개구리 점프

N, Q = map(int, input().split()) # 10만까지
# 시간 초과 1초


log_list = []
for _ in range(N):
    x1, x2, y = map(int, input().split())
    log_list.append((x1, x2, y))

# log_list.sort(key = lambda x: (x[0], x[2]))

for q in range(Q):
    s, e = map(int, input().split())