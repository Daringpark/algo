
H, W = map(int, input().split())
matrix = [list(input()) for _ in range(H)]
result = [[-1] * W for _ in range(H)]

# 사전 구성 미리 출력할 지도에 구름 채우기
for row in range(H):
    for col in range(W):
        if matrix[row][col] == 'c':
            result[row][col] = 0

for row in range(H):
    # 0이 있는 경우만 볼거다.
    if 0 in result[row]:
        # 전체를 다 돌아야하긴 함
        for col in range(W):
            if matrix[row][col] == '.' and result[row][col] == -1:
                if 0<= col-1 < W and result[row][col-1] >= 0:
                    result[row][col] = result[row][col-1] + 1

for row in result:
    print(*row)

'''
6 8
.c......
........
.ccc..c.
....c...
..c.cc..
....c...

'''