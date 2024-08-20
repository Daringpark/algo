
import sys
input = sys.stdin.readline


# 현재 땅을 기준으로 모래를 날려줄 함수
def wind_blow(r, c, nr, nc):
    global result
    # 우선 모래 총 량을 담아둔다.
    sand = matrix[r][c]
    sand_list = [int(sand*0.01), int(sand*0.02), int(sand*0.05),int(sand*0.07), int(sand*0.1)]
    
    # 왼쪽으로 이동
    if nr == 0 and nc == -1:
        for dr, dc in [(-1, 1), (1, 1)]:
            new_row = r + dr
            new_col = c + dc

            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[0]
            else:
                result += sand_list[0]
            sand -= sand_list[0]

        # 옆 처리
        for dr, dc in [(-1, 0), (-2, 0), (1, 0), (2, 0)]:
            new_row = r + dr

            # 2 %
            if dr == 2 or dr == -2:
                if 0 <= new_row < N:
                    matrix[new_row][c] += sand_list[1]
                else:
                    result += sand_list[1]
                sand -= sand_list[1]
            else:
                if 0 <= new_row < N:
                    matrix[new_row][c] += sand_list[3]
                else:
                    result += sand_list[3]
                sand -= sand_list[3]

        # 앞 대각선 처리
        for dr, dc in [(-1, -1), (1, -1)]:
            new_row = r + dr
            new_col = c + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[4]
            else:
                result += sand_list[4]
            sand -= sand_list[4]

        # 앞 처리
        new_col = c - 2
        if 0 <= new_col < N:
            matrix[r][new_col] += sand_list[2]
        else:
            result += sand_list[2]
        sand -= sand_list[2]

        if 0 <= c-1 < N:
            matrix[r][c-1] += sand
        else:
            result += sand

    # 아래으로 이동
    elif nr == 1 and nc == 0:
        for dr, dc in [(-1, -1), (-1, 1)]:
            new_row = r + dr
            new_col = c + dc

            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[0]
            else:
                result += sand_list[0]
            sand -= sand_list[0]

        # 옆 처리
        for dr, dc in [(0, -2), (0, -1), (0, 1), (0, 2)]:
            new_col = c + dc

            # 2 %
            if dc == 2 or dc == -2:
                if 0 <= new_col < N:
                    matrix[r][new_col] += sand_list[1]
                else:
                    result += sand_list[1]
                sand -= sand_list[1]
            else:
                if 0 <= new_col < N:
                    matrix[r][new_col] += sand_list[3]
                else:
                    result += sand_list[3]
                sand -= sand_list[3]

        # 앞 대각선 처리
        for dr, dc in [(1, -1), (1, 1)]:
            new_row = r + dr
            new_col = c + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[4]
            else:
                result += sand_list[4]
            sand -= sand_list[4]

        # 앞 처리
        new_row = r + 2
        if 0 <= new_row < N:
            matrix[new_row][c] += sand_list[2]
        else:
            result += sand_list[2]
        sand -= sand_list[2]

        if 0 <= r+1 < N:
            matrix[r+1][c] += sand
        else:
            result += sand

    # 오른쪽으로 이동
    if nr == 0 and nc == 1:
        for dr, dc in [(-1, -1), (1, -1)]:
            new_row = r + dr
            new_col = c + dc

            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[0]
            else:
                result += sand_list[0]
            sand -= sand_list[0]

        # 옆 처리
        for dr, dc in [(-1, 0), (-2, 0), (1, 0), (2, 0)]:
            new_row = r + dr

            # 2 %
            if dr == 2 or dr == -2:
                if 0 <= new_row < N:
                    matrix[new_row][c] += sand_list[1]
                else:
                    result += sand_list[1]
                sand -= sand_list[1]
            else:
                if 0 <= new_row < N:
                    matrix[new_row][c] += sand_list[3]
                else:
                    result += sand_list[3]
                sand -= sand_list[3]

        # 앞 대각선 처리
        for dr, dc in [(-1, 1), (1, 1)]:
            new_row = r + dr
            new_col = c + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[4]
            else:
                result += sand_list[4]
            sand -= sand_list[4]

        # 앞 처리
        new_col = c + 2
        if 0 <= new_col < N:
            matrix[r][new_col] += sand_list[2]
        else:
            result += sand_list[2]
        sand -= sand_list[2]

        if 0 <= c+1 < N:
            matrix[r][c+1] += sand
        else:
            result += sand

    # 위로 이동
    elif nr == -1 and nc == 0:
        # 뒤
        for dr, dc in [(1, -1), (1, 1)]:
            new_row = r + dr
            new_col = c + dc

            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[0]
            else:
                result += sand_list[0]
            sand -= sand_list[0]

        # 옆 처리
        for dr, dc in [(0, -1), (0, -2), (0, 1), (0, 2)]:
            new_col = c + dc

            # 2 %
            if dc == 2 or dc == -2:
                if 0 <= new_col < N:
                    matrix[r][new_col] += sand_list[1]
                else:
                    result += sand_list[1]
                sand -= sand_list[1]
            else:
                if 0 <= new_col < N:
                    matrix[r][new_col] += sand_list[3]
                else:
                    result += sand_list[3]
                sand -= sand_list[3]

        # 앞 대각선 처리
        for dr, dc in [(-1, -1), (-1, 1)]:
            new_row = r + dr
            new_col = c + dc
            if 0 <= new_row < N and 0 <= new_col < N:
                matrix[new_row][new_col] += sand_list[4]
            else:
                result += sand_list[4]
            sand -= sand_list[4]

        # 앞 처리
        new_row = r - 2
        if 0 <= new_row < N:
            matrix[new_row][c] += sand_list[2]
        else:
            result += sand_list[2]
        sand -= sand_list[2]

        if 0 <= r-1 < N:
            matrix[r-1][c] += sand
        else:
            result += sand

def move():
    row, col = m, m
    step = 1
    # 1, 1에 도달한 순간 break
    while row != 0 or col != N-1:
        # 홀수는 왼쪽, 아래 이동
        if step%2:
            for dr, dc in [(0, -1), (1, 0)]:
                for _ in range(step):
                    row += dr
                    col += dc
                    # print(row, col)
                    # 값이 있어야 모래도 이동을 하지...
                    if matrix[row][col]:
                        wind_blow(row, col, dr, dc)
            step += 1
        
        # 짝수는 오른쪽, 위 이동
        else:
            for dr, dc in [(0, 1), (-1, 0)]:
                for _ in range(step):
                    row += dr
                    col += dc
                    # print(row, col)
                    if matrix[row][col]:
                        wind_blow(row, col, dr, dc)
            step += 1

    # N-1만큼의 추가 이동
    # 마지막, 추가로 왼쪽 이동을 진행해야함.
    if step == N:
        for _ in range(N-1):
            col -= 1
            # print(row, col)
            if matrix[row][col]:
                wind_blow(row, col, 0, -1)

# 500 * 500 

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 토네이도가 움직이는 함수, 그 안에 모래를 날릴 함수
m = N//2
result = 0
move()

# 격자 밖으로 나간 모래의 양을 출력한다.
print(result)