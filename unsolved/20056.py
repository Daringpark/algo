
# 20056 마법사 상어와 파이어볼

N, M, K = map(int, input().split())
# M줄은 N^2 까지 주어질 수 있다.

drdc = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
matrix = [[[] for _ in range(N)] for _ in range(N)]

print(matrix)
for _ in range(M):
    row, col, mass, speed, direction = map(int, input().split())
    # 위치가 같은 경우는 주어지지 않는다! 아싸
    matrix[row-1][col-1] = [mass, speed, direction]

for row in matrix:
    print(*row)




for _ in range(K):
    
    # N = 50 이하
    for row in range(N):
        for col in range(N):
            
            # 리스트가 채워져 있다면?
            if matrix[row][col]:
                row += 