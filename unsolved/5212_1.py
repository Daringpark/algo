
# 5212 지구온난화
M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
change_list = []

for row in range(M):
    for col in range(N):
        if matrix[row][col] == 'X':
            sea_count = 0

            # 1.) 테두리 부분 챙기기
            if row == 0 or row == M-1:
                sea_count += 1
            if col == 0 or col == N-1:
                sea_count += 1

            # 2.) 현재 칸 기준으로 유효한 칸의 바다 찾기
            for dr,dc in drdc:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < M and 0 <= new_col < N:
                    if matrix[new_row][new_col] == '.':
                        sea_count += 1
            if sea_count >= 3:
                change_list.append((row, col))

def Sink(maps, y, x):
    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
 
        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            cnt += 1 # 영역 밖은 바다로 취급
            continue
        if maps[ny][nx] == '.':
            cnt += 1
    if cnt >= 3:
        convert.append((y, x))
 
for onStart in start:
    Sink(maps,onStart[0], onStart[1])
 
for obj in convert:
    y, x = obj[0], obj[1]
    maps[y][x] = '.'
    start.remove((y,x))
 
minR, minC = start[0]
maxR, maxC = start[0]
 
for obj in start:
    y, x = obj[0], obj[1]
    if y < minR:
        minR = y
    elif y > maxR:
        maxR = y
    if x < minC:
        minC = x
    elif x > maxC:
        maxC = x
 
for j in range(minR, maxR + 1):
    result = ''
    for i in range(minC, maxC + 1):
        result += maps[j][i]
        # print(*maps[j][i], end='')
    print(result)
