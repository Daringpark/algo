
# BOJ 골드 1959 달팽이 3
# 연산으로 처리해야 함. 패턴 파악하기




# 5 3
N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
row, col = 0, 0

d = 0
drdc = [[0,1], [1,0], [0,-1], [-1,0]]
while True:

    dr, dc = drdc[d]
    new_row = row + dr
    new_col = col + dc
    if 0 <= new_row < N and 0 <= new_col < M:
        if not visited[new_row][new_col]:
            visited[new_row][new_col] = 1
            row = new_row
            col = new_col

    if new_row > N:
        d = 1
    elif new_col > M:
        d = 2
    elif new_row < 0:
        d = 3
    elif visited[new_row][new_col] and d == 3:
        d = 0
