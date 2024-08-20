
import sys
sys.stdout = open('4963_output.txt' , 'w')

import sys
input = sys.stdin.readline
drdc = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
def find_island():
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j]: # 어 섬 발견
                stack = [[i,j]]
                while stack:
                    x, y = stack.pop()
                    matrix[x][y] = 0
                    for dx, dy in drdc:
                        new_x = x + dx
                        new_y = y + dy
                        if 0 <= new_x < h and 0 <= new_y < w:
                            if matrix[new_x][new_y]: # 1인 경우
                                stack.append([new_x, new_y])
                cnt += 1
    return cnt    
while True:
    w, h = map(int, input().split())
    if h == 0 and w == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    print(find_island())
#     print(matrix)


'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
0 0
'''