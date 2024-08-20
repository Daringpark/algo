
# 1913 달팽이 (실버 3)

# 홀수 자연수 >> 방향성이 정해져있음
N = int(input())
M = int(input())

matrix = [[0] * N for _ in range(N)]
row, col = N//2, N//2
matrix[row][col] = 1
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
d = 0
level = 1

n = 2
# 1, 1
res = [row+1, col+1]
while row != 0 or col != 0: 
    flag = 0
    # 위, 오, // 아, 아, 왼, 왼,// 위 위 위, 오 오 오,// 아 아 아 아, 왼 왼 왼 왼
    for _ in range(2):
        for _ in range(level):
            row += drdc[d][0]
            col += drdc[d][1]
            matrix[row][col] = n
            if n == M:
                # 바꿔주기
                res = [row+1, col+1]
            if row == 0 and col == 0: # 다 돌고 끝까지 왔을 때,
                flag = 1
                break
            n += 1
        if flag == 1: # 방향 바꾸기 전에
            break
        # 방향 바꿔주기
        d = (d+1)%4
    level += 1
for r in matrix:
    print(*r)
print(*res)