# BOJ 18430
# BackTracking

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

boomerangs = [
    [(0, 0), (-1, 0), (0, 1)],  # 위 + 오른쪽
    [(0, 0), (0, 1), (1, 0)],   # 오른쪽 + 아래
    [(0, 0), (1, 0), (0, -1)],  # 아래 + 왼쪽
    [(0, 0), (0, -1), (-1, 0)]  # 왼쪽 + 위
]

max_value = 0

def dfs(r, c, total):
    global max_value

    if c == M:
        r += 1
        c = 0
    if r == N:
        max_value = max(max_value, total)
        return
    
    if not visited[r][c]:
        for b in boomerangs:
            flag = True
            cells = []
            val = 0
            for dr, dc in b:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    cells.append((nr, nc))
                else:
                    flag = False
                    break
            
            if flag:
                for idx, (nr, nc) in enumerate(cells):
                    visited[nr][nc] = 1
                    if idx == 0:
                        val += matrix[nr][nc] * 2 # 중심은 2배
                    else:
                        val += matrix[nr][nc]
                dfs(r, c+1, total + val)
                for nr, nc in cells:
                    visited[nr][nc] = 0

    dfs(r, c+1, total)  # 부메랑을 놓지 않는 경우

dfs(0, 0, 0)
print(max_value)