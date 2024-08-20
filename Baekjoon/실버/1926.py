

'''
5 5
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
'''
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
def dfs(lst):
    global max_bulk
    stack = [lst]
    matrix[lst[0]][lst[1]] = 0
    value = 1

    while stack:
        item = stack.pop()
        row, col = item[0], item[1]
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < M and 0 <= new_col < N:
                if matrix[new_row][new_col]:
                    matrix[new_row][new_col] = 0
                    stack.append([new_row, new_col])
                    value += 1
    max_bulk = max(max_bulk, value)

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
max_bulk = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j]:
            cnt += 1
            dfs([i, j])
print(cnt)
print(max_bulk)