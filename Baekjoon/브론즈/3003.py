# 3003번 체스 말 갯수 맞추기
import sys
input = sys.stdin.readline

chess_box = [1, 1, 2, 2, 2, 8]
check_box = list(map(int, input().split()))

for i in range(len(chess_box)) :
    if check_box[i] == chess_box[i] :
        check_box[i] = 0
    else :
        check_box[i] = chess_box[i] - check_box[i]
    print(check_box[i], end = ' ')