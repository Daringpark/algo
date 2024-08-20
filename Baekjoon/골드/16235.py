
# 백준 16235 나무 제테크

# 모듈
import sys
input = sys.stdin.readline
# N = matrix 크기 (r, c는 1부터 시작해서 N까지)
N, M, K = map(int, input().split())
# N은 10이하, M은 100 이하, K는 1000이하

# 로봇이 겨울에 땅에 주는 양분의 양
matrix = [list(map(int, input().split())) for _ in range(N)]
# 값은 100까지 있을 수 있다.

# 초기 세팅 : 가장 처음 양분은 각각 땅의 5로 시작한다.
# 여러개의 나무가 있다 ? << 양분 배열을 따로 줘야한다.
tree_matrix = [[[] for _ in range(N)] for _ in range(N)]
death_tree = [[[] for _ in range(N)] for _ in range(N)]
soil_matrix = [[5] * N for _ in range(N)]

# Z는 10 이하
for _ in range(M):
    x, y, z = map(int, input().split()) # x, y는 나무의 위치 (r, c); z는 나무의 나이
    tree_matrix[x-1][y-1].append(z)

drdc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# for i in range(N):
#     print(*tree_matrix[i])
def spring():
    for row in range(N):
        for col in range(N):
            # 최소 10개 있다고 가정하면, 10*1000*100 = 10**6
            if tree_matrix[row][col]: # 비어 있는 리스트가 아니라면,
                tree_matrix[row][col].sort() # 우선 순위를 주기 위해서
                n = len(tree_matrix[row][col])
                temp_t = []
                temp_d = []
                for i in range(n):
                    if soil_matrix[row][col] - tree_matrix[row][col][i] < 0:
                        temp_d.append(tree_matrix[row][col][i])
                    else:
                        soil_matrix[row][col] -= tree_matrix[row][col][i]
                        temp_t.append(tree_matrix[row][col][i]+1)
                tree_matrix[row][col] = temp_t
                death_tree[row][col] = temp_d

# 봄에 죽은 나무는 현재 땅의 양분으로 추가된다.
# 완료
def summer():
    for row in range(N):
        for col in range(N):
            if death_tree[row][col] != []: # 리스트 값이 있으면, == 죽은 나무가 있으면
                for death in death_tree[row][col]:
                    soil_matrix[row][col] += int(death/2)
                death_tree[row][col] = []

# 나이가 5의 배수인 나무는 번식을 한다. (주변 8칸에 수명이 1인 나무 생성)
# 완료
def fall():
    for row in range(N):
        for col in range(N):
            for tree in tree_matrix[row][col]:
                if tree%5 == 0: # 5의 배수인 나무 찾았다.
                    for dr, dc in drdc:
                        new_row = row + dr
                        new_col = col + dc

                        if 0 <= new_row < N and 0 <= new_col < N:
                            # extend? tree_matrix[new_row][new_col] = [1] + tree_matrix[new_row][new_col]
                            tree_matrix[new_row][new_col].append(1)

# 겨울에는 각 땅에 로봇이 matrix에 저장한 양분만큼 현재 땅의 양분을 추가해준다.
# 완료
def winter():
    for row in range(N):
        for col in range(N):
            soil_matrix[row][col] = soil_matrix[row][col] + matrix[row][col]

# K번의 순회 (1년 주기)
# O(K*N**2 == 100000)
for k in range(K):
    spring()
    # 디버깅
    # print(f'{k} spring')
    # for i in range(N):
    #     print(*tree_matrix[i])
    summer()
    fall()
    winter()
    # 디버깅
    # print(f'{k} winter')
    # for i in range(N):
    #     print(*soil_matrix[i])

cnt = 0
for i in range(N):
    for j in range(N):
        if tree_matrix[i][j]: # 나무가 살아 있다면,
            cnt += len(tree_matrix[i][j])
print(cnt)