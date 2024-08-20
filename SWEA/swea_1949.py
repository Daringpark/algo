
'''
1      
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8

6
'''
## SWEA 1949 등산로 조정

def find_max():
    # 산봉우리 탐색을 위한 최대값 발견하기
    max_value = 0 # 처음 지도에서 나타나는 높이는 1보다 낮을 수 없다.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
    
    # 찾았으면, 이제 그 값에 해당하는 시작점을 찾자.
    start = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_value:
                start.append((i, j))
    return start

def dfs(row, col, flag, cnt):
    global res
    
    # 매 번 갱신
    if cnt > res:
        res = cnt

    visited[row][col] = 1

    # 지금 있는 부분이 제일 낮은 부분인가?
    for dr, dc in drdc:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < N and 0 <= new_col < N:
            # 일반 재귀를 도는 경우
            if not visited[new_row][new_col]:
                if matrix[row][col] > matrix[new_row][new_col]:
                        dfs(new_row, new_col, flag, cnt + 1)
                
                # 아직 등산로 조성을 하지 않았을 경우,
                elif flag == 0 and matrix[row][col] > matrix[new_row][new_col] - K:
                    origin = matrix[new_row][new_col]
                    # 바로 한 칸만 깎아주기 (경로 최대 길이를 보려면 어차피 K가 높아서 많이 깎아도 의미 없다)
                    matrix[new_row][new_col] = matrix[row][col] - 1
                    dfs(new_row, new_col, 1, cnt + 1)
                    matrix[new_row][new_col] = origin

    # return 이전 원복시키기
    visited[row][col] = 0

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    # K만큼 깎아야함. (그 이하 그 이상도 아니고 딱 그 값으로)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    drdc = [(-1,0), (0,1), (1,0), (0,-1)]

    res = 1
    # matrix의 높은 봉우리는 최대 5개
    for i, j in find_max():
        visited = [[0] * N for _ in range(N)]
        dfs(i, j, 0, 1)

    print(f'#{tc} {res}')