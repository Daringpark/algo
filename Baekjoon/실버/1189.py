
def dfs(r, c, dist):
    global result
    if dist == K:
        if r == 0 and c == C-1:
            result += 1
            return
        
    matrix[r][c] = 'T'
    for dr, dc in drdc:
        new_row = r + dr
        new_col = c + dc
        if 0 <= new_row < R and 0 <= new_col < C:
            if matrix[new_row][new_col] == '.':
                matrix[new_row][new_col] = 'T'
                dfs(new_row, new_col, dist+1)
                matrix[new_row][new_col] = '.'

# 초기 세팅
R, C, K = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# DFS 탐색
result = 0
dfs(R-1, 0, 1)

print(result)