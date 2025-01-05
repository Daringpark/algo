
def move_cloud(row, col, dr, dc, s):
    for _ in range(s):
        row += dr
        col += dc

        if row >= N:
            row = 0
        elif row < 0:
            row = N-1

        if col >= N:
            col = 0
        elif col < 0:
            col = N-1

    return row, col

# begin with index 1 - 8
drdc = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split()) )for _ in range(M)]

'''
1. 이동
    - 범위를 넘으면 이어져있다고 생각하고 넘길 것
    - N,3에서 아래로 내려갈 경우 -> 1,3으로 이동
2. 구름에서 물 뿌려주기
3. 구름이 사라지기
4. 물 복사 (구름 때문에 물이 증가했던 칸에서는 대각선 방향으로 체크 - 물의 양을 체크)
    - 이때 범위를 철저하게 지킬 것
5. 물이 2 이상 있는 위치에서 구름 생성, 구름이 있었던 위치에서는 구름이 생성되지 않음
'''

# 시작 구름 (0부터 N-1까지 시작 = 문제에서는 1부터 N까지)
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

# 1.이동
for d, s in order:
    # 이동 이후, 구름 위치
    new_cloud = []

    # 변화 방향
    dr, dc = drdc[d]
    for row, col in cloud:
        '''
        s만큼 이동을 해야하고 (반복문)
        이동 + 변환 = 1회
        이동 -> 변환 -> 이동 -> 변환
        
        new_row = row + dr
        new_col = col + dc
        '''
        new_row, new_col = move_cloud(row, col, dr, dc, s)
        new_cloud.append((new_row, new_col))

    # 2.물 뿌리기
    for nr, nc in new_cloud:
        matrix[nr][nc] += 1

    # 3.구름 없애기; 새로운 구름 만들기 + 기억하고 있는 구름은 new_cloud
    cloud = []

    # 4.물 복사
    for r, c in new_cloud:
        for i in range(2, 9, 2):
            dr,dc = drdc[i]
            nr = r + dr
            nc = c + dc
            # 범위 안에 있거나 물이 있으면
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] > 0:
                    matrix[r][c] += 1

    # 5. 물이 2이상인 곳에서 구름 생성 (new_cloud에 있었던 칸은 안됨)
    for row in range(N):
        for col in range(N):
            if matrix[row][col] >= 2:
                if (row, col) not in new_cloud:
                    cloud.append((row, col))
                    matrix[row][col] -= 2

    # print("-"*N)
    # for i in range(N):
    #     print(*matrix[i])
    # print("-"*N)


result = 0
for row in matrix:
    result += sum(row)

print(result)