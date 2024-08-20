
# 5212 지구 온난화

M, N = map(int, input().split())
matrix = [list(input()) for _ in range(M)]

drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 1. 바꿔줄 육지 찾기
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

# 2. 육지 한번에 바꾸고 시작 row,col, 끝 row,col을 찾기
for row, col in change_list:
    matrix[row][col] = '.'

# for row in matrix:
#     print(*row)
row_set = set()
col_set = set()
for row in range(M):
    for col in range(N):
        if matrix[row][col] == 'X':
            row_set.add(row)
            col_set.add(col)

if row_set:
    start_row = min(row_set)
    end_row = max(row_set)
    start_col = min(col_set)
    end_col = max(col_set)

    # 3. 바꾼 지도를 기준으로 출력하기
    # 한 개 이상은 있다고 한다.
    for row in range(start_row, end_row + 1):
        print(''.join(matrix[row][start_col:end_col + 1]))