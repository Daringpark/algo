# 만약 코어가 3개가 있을 때.... 4방향 모두 선택하는 모든 경우의 수 구해보기
# 부분집합 구하듯이...특정 상황에서 할 수 있는 모든 경우의수를 다 해보기

# 상하 좌우 탐색을 위한 변화량 배열
di = [-1,1,0,0]
dj = [0,0,-1,1]

# n: 코어번호
# d : 전선 연결 방향  #상하좌우
# 반환 : 연결된 전선의 길이
def connect(n,d):
    #전선을 연결하려는 방향을 모두 확인
    #전선을 연결할 수 있는 경우 전선을 연결
    #1. 전선이 d 방향으로 연결될 수 있는지 확인
    # 코어의 위치
    i, j = cores[n]
    ni, nj = i + di[d], j + dj[d]
    #연결 되려면 전선이 있거나 코어가 있으면 안됨
    while 0 <= ni < N and 0<= nj < N and data[ni][nj] == 0:
        ni = ni + di[d]
        nj = nj + dj[d]
    #연결 가능한 조건은 ni, nj가 범위를 벗어났으면 d방향으로 전선 연결 가능
    cnt = 0
    # 한 칸씩 이동하면서 전선 위치에 2넣어주기
    if ni < 0 or ni >=N or nj < 0 or nj >=N:
        ni, nj = i + di[d], j + dj[d]
        while 0 <= ni < N and 0 <= nj < N:
            data[ni][nj] = 2
            cnt += 1
            ni = ni + di[d]
            nj = nj + dj[d]


    return cnt
# n: 코어번호
# d : 전선 연결 방향
def disconnect(n,d):
    i, j = cores[n]
    ni, nj = i + di[d], j + dj[d]
    while 0 <= ni < N and 0 <= nj < N:
        data[ni][nj] = 0
        ni = ni + di[d]
        nj = nj + dj[d]


# 특정 코어에서 전선을 연결 할 수 있는 모든 방향으로 연결해보기
# idx : 코어 번호
# num : 연결한 코어의 개수
# length : 사용한 전선의 길이

#어떤 코어를 한 방향으로 전선 연결해보기
def solve(idx,num,length):
    global max_core,min_length
    if idx == len(cores):
        #최대 코어개수 찾기 + 최소길이 전선 찾기
        if num > max_core:
            max_core = num
            min_length = length
        elif num == max_core and length < min_length:
            min_length = length
        return
    #idx 번째 코어에 대해서 네 방향 전선 연결 해보기
    for i in range(4):  # i = 전선연결하는 방향
        # i번 방향으로 전선 연결 해보기
        # tmp : i방향으로 연결했을때, 전선의 길이 , 0 이라면 연결 불가능
        tmp = connect(idx,i)
        if tmp > 0: #연결 했으면...
            solve(idx+1,num + 1,length + tmp)
            # i 번 방향으로 전선 연결된거 없애기
            disconnect(idx,i)
    #연결 안한 경우의 수도 포함
    solve(idx + 1, num, length)

# 최대 코어 개수, 
# 최소 전선 길이
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    cores = []
    #연결 대상 core 들의 위치 저장하기
    # 가장자리에 위치한 core는 이미 연결된 core이기 때문에 제외
    max_core = 0
    min_length = 1000000
    for i in range(1,N-1):
        for j in range(1,N-1):
            if data[i][j]:
                cores.append((i, j))

    solve(0,0,0)
    print(f'#{tc} {min_length}')
