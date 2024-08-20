
'''
2 20 50
50 30
20 40

1
'''
from collections import deque
# 시간 제한 2초 : 40,000,000

def bfs():
    global cnt
    flag = 0
    visited = [[0] * N for _ in range(N)]
    party_list = []
    for i in range(N):
        for j in range(N):


            queue = deque()
            if not visited[i][j]: # 방문하지 않았던 (BFS를 돌았지 않았던 곳이면)
                queue.append([i, j])
            visited[i][j] = 1
            
            party = []
            s = 0
            while queue:
                row, col = queue.popleft()

                party.append([row, col])
                s += matrix[row][col]
                for dr, dc in drdc:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < N and 0 <= new_col < N:
                        diff = abs(matrix[row][col] - matrix[new_row][new_col])
                        if not visited[new_row][new_col]: # 내 딛을 곳을 방문 안했다면
                            if L <= diff <= R:
                                visited[new_row][new_col] = 1
                                queue.append([new_row, new_col])
            # while문을 빠져 나온다. << 이어져있는거 확인 완료
            if len(party) > 1: # 본인 왕국만 있는게 아니라 평균을 내야할 때
                flag = 1
                party.append(int(s/len(party)))
                party_list.append(party)

    if party_list:
        for p in party_list:
            for i in range(len(p)-1):
                r, c = p[i][0], p[i][1]
                matrix[r][c] = p[-1]
        cnt += 1

    return flag

# 초기 세팅과 입력 받기
N, L, R = map(int, input().split()) # LR 1 ~ 100
matrix = [list(map(int, input().split())) for _ in range(N)] # 50 * 50
drdc = [[-1,0], [0,1], [1,0], [0,-1]]
cnt = 0

while True:
    if not bfs():
        break
print(cnt)