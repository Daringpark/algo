# 2564 - 경비원

def to_linear_pos(direction, pos):
    return {
        1: lambda x: x,                  # 북쪽
        2: lambda x: 2*M + N - x,        # 남쪽
        3: lambda x: 2*(M + N) - x,      # 서쪽
        4: lambda x: M + x               # 동쪽
    }[direction](pos)

M, N = map(int, input().split())
n = int(input())

markets = []
for _ in range(n):
    d, p = map(int, input().split())
    markets.append(to_linear_pos(d, p))

guard_dir, guard_pos = map(int, input().split())
guard = to_linear_pos(guard_dir, guard_pos)

total_length = 2 * (M + N)

result = 0
for store in markets:
    diff = abs(store - guard)
    result += min(diff, total_length - diff)

print(result)