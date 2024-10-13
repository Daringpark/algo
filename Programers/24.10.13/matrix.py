

# board[row][col] 위치의 상하좌우를 확인하여, 같은 색깔이면 count ++
def solution(board, h, w):
    answer = 0

    # 정사각형이라고 문제에서 정의
    n = len(board)

    # 바라볼 방향을 설정
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    # 우, 하, 상, 좌 순으로 i를 돌려가며 확인한다.
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        # 유효한 board 안에 있는지 범위 체크
        if 0 <= h_check < n and 0 <= w_check < n:
            # 실제 맞는지 아닌지 체크
            if board[h][w] == board[h_check][w_check]:
                answer += 1

    return answer