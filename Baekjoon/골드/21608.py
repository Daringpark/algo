
import sys
input = sys.stdin.readline

def find_seat(number, lst):

    # 400 * 1600
    # 비어있는 칸 중에서 좋아하는 학생이 가장 많이 카운트 되는 칸에 배치
    count_matrix = [[0] * N for _ in range(N)]
    # 좋아하는 친구를 하니씩 꺼내서 칸에 선호도
    for row in range(N):
        for col in range(N):
            for item in lst:
                # 친구를 찾았다! == 인접칸에 선호도 + 1
                if matrix[row][col] == item:
                    for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < N and 0 <= new_col < N:
                            if not matrix[new_row][new_col]:
                                count_matrix[new_row][new_col] += 100
                elif matrix[row][col] == 0:
                    for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < N and 0 <= new_col < N:
                            if not matrix[new_row][new_col]:
                                count_matrix[new_row][new_col] += 1

    # 만들어진 카운트 matrix를 기준으로 비어있는 칸이 가장 많은 칸을 구한다.
    
    # 1. 카운트가 많은 칸을 우선 구한다.
    max_cnt = 0
    temp = []
    for row in range(N):
        for col in range(N):
            if count_matrix[row][col] > max_cnt:
                max_cnt = count_matrix[row][col]
                temp = [(row, col)]
            elif count_matrix[row][col] == max_cnt:
                temp.append((row, col))

    
    for row, col in temp:
        if not visited[row][col]:
            matrix[row][col] = number
            visited[row][col] = 1
            break
    # 카운트가 겹친다면, 비어있는 칸이 많은 칸으로 간다.
    # 비어있는 칸도 겹친다면, dr,dc 순으로 간다.
    
    # 디버깅
    # for row in matrix:
    #    print(*row)

# matrix는 N^2
N = int(input())
matrix = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 상, 좌, 우, 하
# drdc = [(-1,0), (0,-1), (0,1), (1,0)]

# N^2의 입력을 받아온다.
friends = dict()
for _ in range(N**2):
    # 학생 번호와 좋아하는 4명의 학생
    student, s1, s2, s3, s4= map(int, input().split())
    friends.setdefault(student, (s1, s2, s3, s4))
    # matrix를 확인하고, 학생을 배치해야함.
    find_seat(student, friends[student])


# 배치가 다 끝나게 되면, row, col 순회를 통해서 만족도 조사를 해야한다.
# complexity  : 400 * 4 
result = 0
for row in range(N):
    for col in range(N):
        student = matrix[row][col]
        cnt = 0
        for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < N and 0 <= new_col < N :
                if matrix[new_row][new_col] in friends[student]:
                    cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)
print(result)