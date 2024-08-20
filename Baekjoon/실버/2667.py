# N = 7
# Matrix
from collections import deque
drdc = [[-1,0], [0,1], [1,0], [0,-1]]

def BFS(arr):
    matrix = arr
    
    plus = -1
    apartments = list()
    for i in range(N): # 함수 내부에서 돌린다.
        for j in range(N):
            
            if matrix[i][j] == 1 and not visited[i][j]: # 인접 값을 찾는 조건
                
                plus += 1
                queue = deque([[i,j,matrix[i][j]+plus]]) # 초기 지점 넣고 시작
                visited[i][j] = matrix[i][j]+plus
                cnt = 1
                
                while queue: # 인접 값을 다 돌고 나오면 다시 반복문을 돌게 된다.
                    item = queue.popleft()
                    for row, col in drdc:
                        
                        new_row = item[0] + row
                        new_col = item[1] + col
                        if 0 <= new_row < N and 0 <= new_col < N:
                        
                            if matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
                                visited[new_row][new_col] = item[2]
                                queue.append([new_row, new_col, visited[new_row][new_col]])
                                cnt += 1
                apartments.append(cnt)
            
    if not apartments:
        print(0)
    else:
        print(item[2]) # 제일 마지막에 들어갔던 값이 단지 수가 됨
        apartments.sort()
        for numbers in apartments:
            print(numbers)

N = int(input())
Matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)] # 방문처리를 통해서 중복해서 덧씌우지 않게
BFS(Matrix)
# 총 단지 수를 출력하고, 단지의 수를 오름차순 정렬해서 출력한다. 3, (8,7,6) > 3, (6,7,8)

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

5
00100
00111
00000
11110
00000
'''