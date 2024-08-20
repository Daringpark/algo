
# 0,0 1,1 > 1칸 (1,5) 칸까지가 영역으로 쓰일 수 있음
# 0,0 1,1 > M-1 row, 0 (1-1) col
# 0,2 4,4
# 1,1 2,5
# 4,0 6,2

# 왼쪽 아래가 0,0 오른쪽 위가 N,M (M-M, N-N)
# 0 , 2 >> M - (M-0), N - (N-2) 
# 2 5 >> M 5 - 2, N 7 - 5
# M*N = 10**4*K(10**2) = 1e6

def dfs():
    global cnt_list
    
    for i in range(M):
        for j in range(N):
            cnt = 0
            if not matrix[i][j]:
                cnt += 1
                stack = [[i,j]]
                matrix[i][j] = 1
                
                while stack:
                    item = stack.pop()
                    row, col = item[0], item[1]
                    for dr,dc in drdc:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < M and 0 <= new_col < N:
                            if not matrix[new_row][new_col]:
                                matrix[new_row][new_col] = 1
                                stack.append([new_row, new_col])
                                cnt += 1
            if cnt:
                cnt_list.append(cnt)

M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
for k in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())
    
    for i in range(M-end_y, M-start_y):
        for j in range(start_x, end_x):
            matrix[i][j] += 1            
    # for i in range(M):
    #     print(*matrix[i])
cnt_list = []
dfs()
cnt_list.sort()

print(len(cnt_list))
print(*cnt_list)