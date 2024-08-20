
# 직사각형이 나오는 경우 a
# 직선이 나오는 경우 b
# 점이 나오는 경우 c
# 겹치는 점이 하나도 없는 경우 d

    # 상대 축 만들기 ??
    # (3,10) -- (200,300)
    # 198 200-3+1
    
    # 0 1 2 3
    # 
    
    # 4 5 6 7
    # 
'''
3 10 50 60 100 100 200 300
'''

import sys
input = sys.stdin.readline

# for _ in range(4):
for _ in range(4):
    square = list(map(int, input().split()))
    max_X = max(square[2], square[6])
    min_X = min(square[0], square[4])
    max_Y = max(square[3], square[7])
    min_Y = min(square[1], square[5])
    # matrix 0 2 4 6 X축 결정
    # matrix 1 3 5 7 Y축 결정
    
    x_axis = [0]*(max_X-min_X)
    y_axis = [0]*(max_Y-min_Y)
    print(max_X, max_Y, min_X, min_Y)
    for i in range(4):
        square[2*i] -= min_X
        square[2*i+1] -= min_Y
    row = max_Y-min_Y
    col = max_X-min_X
    # Y가 row, X가 col

    new_matrix = [[0]*col for _ in range(row)]
    

    for i in range(max_Y):
        if 2 in new_matrix[i]:
