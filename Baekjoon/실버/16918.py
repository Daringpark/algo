
# BOJ 16918 봄버맨 실버 1
from collections import deque
def launch_the_bomb(que, matrix):

    while que:
        row, col = que.popleft()
        # 자기 자신을 터트린다.
        matrix[row][col] = '.'
        for dr, dc in drdc:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < R and 0 <= new_col < C:
                if matrix[new_row][new_col] == 'O':
                    matrix[new_row][new_col] = '.'

    for row in range(R):
        for col in range(C):
            if matrix[row][col] == 'O':
                que.append((row, col))
    return que, matrix

# 처음에 초기 상태를 받아야 한다
# 처음 폭탄 위치를 따로 배열에 저장
R, C, T = map(int, input().split())
# 문자열로 넣어줄 예정
bomb_matrix = [list(input().strip()) for _ in range(R)]
drdc = [(-1,0), (0,1), (1,0), (0,-1)]
history = deque()

for i in range(R):
    for j in range(C):
        if bomb_matrix[i][j] == 'O':
            # 타이머가 찬 게 터트리는 주기를 위해서 그것을 history_queue에 넣어준다.
            history.append((i, j))

# 놓고, 기다리고(놓고), 터트리고(1),
# 기다리고(놓고), 터트리고(2),
# 기다리고(놓고), 터트리고(4),
# 기다리고, 터트리고(6),
# T초를 직접 잰다. 1초부터 T초까지
for t in range(2, T+1):
    # 현재 터지는 시간 t가 홀수이면 폭탄을 터트려야한다.
    if t%2 ==1:
        history, bomb_matrix = launch_the_bomb(history, bomb_matrix)

    # 터지는 타이밍이 아니라면, 놔줘야한다. (빈자리에 폭탄을 채워준다.)
    # 이미 history에 시간을 지나가고 있는 폭탄이 존재하기에 그냥 전체 matrix를 폭탄으로 채워주자
    else:
        bomb_matrix = [['O'] * C for _ in range(R)]

# 출력단
for row in bomb_matrix:
    result_row = ''
    for col in range(C):
        result_row += ''.join(row[col])
    print(result_row)

