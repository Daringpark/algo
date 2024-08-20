
import sys
input = sys.stdin.readline

def dust_making():
    
    # 동시에 일어난다. 라는게 조건
    dust_list = []

    # row, col 담아두고, 
    for row in range(R):
        for col in range(C):
            if matrix[row][col] >= 5:
                # 해당되는 좌표랑 값까지 받아서
                dust_list.append((row, col, matrix[row][col]))

    for row, col, amount in dust_list:
        m = amount // 5
        if m > 0:
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < R and 0 <= new_col < C:
                    if matrix[new_row][new_col] != -1:
                        matrix[new_row][new_col] += m
                        matrix[row][col] -= m

def circulation():

    for i in range(2):
        dist_row, dist_col = aircon[i]
        # 아래 방향 청정기
        if i%2:
            row = dist_row + 1
            col = 0 
            matrix[row][col] = 0
            flag = 2
            
            # 위 방향에 도달시 종료
            # 확인, 이동시키기
            while not (row == dist_row and col == 1):
                # 현재 위치는 row, col; 바라보는 방향 new_r, new_c
                dr, dc = drdc[flag]
                new_row = row + dr
                new_col = col + dc
                if dist_row <= new_row < R and 0 <= new_col < C:
                    matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]
                    row, col = new_row, new_col
                # 범위를 벗어남
                else:
                    flag = (flag-1)%4
                    dr, dc = drdc[flag]
                    new_row = row + dr
                    new_col = col + dc
                    matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]
                    row, col = new_row, new_col

        # 위 방향 청정기
        else:
            # 윗 방향 청정기 포지션
            row = dist_row - 1
            col = 0
            matrix[row][col] = 0
            flag = 0

            # 위 방향에 도달시 종료
            # 확인, 이동시키기
            while not (row == dist_row and col == 1):
                # 현재 위치는 row, col; 바라보는 방향 new_r, new_c
                dr, dc = drdc[flag]
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < dist_row+1 and 0 <= new_col < C:
                    matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]
                    row, col = new_row, new_col
                # 범위를 벗어남
                else:
                    flag = (flag+1)%4
                    dr, dc = drdc[flag]
                    new_row = row + dr
                    new_col = col + dc
                    matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]
                    row, col = new_row, new_col

R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 공기 청정기 찾기
aircon = []
for i in range(R):
    if matrix[i][0] == -1:
        aircon.append((i, 0))

for _ in range(T):
    # 먼지 불기
    dust_making()

    # 움직여서 빨아들이기
    circulation()
#    for row in matrix:
#        print(*row)

# 출력단
result = 0
for r in range(R):
    for c in range(C):
        if matrix[r][c] > 0:
            result += matrix[r][c]
print(result)