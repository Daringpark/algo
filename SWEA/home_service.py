import sys
sys.stdin = open('input.txt','r')

def solve():
    # 도시의 모든 위치에서 서비스를 제공해 보기
    max_cnt = 0  #최대값 찾아야 하니 최소값으로 초기화
    for i in range(N):
        for j in range(N):
            # (i,j) : 서비스를 제공하는 중심점
            # 각 위치에서 서비스 제공지역 범위를 늘려가면서 계산
            # 서비스의 범위 K : 1 ~ N+1
            for k in range(1, N+2):
                cost = k*k +(k-1)*(k-1)
                #서비스 제공 지역에 몇 개의 집이 있는지 확인
                # 모든 지역을 검사하면서...집과 중심점의 거리가 k이하인지 확인
                # 서비스를 제공할 수 있는 집의 개수를 세기
                cnt = 0 #서비스 영역안에 있는 집의 개수
                for a in range(N):
                    for b in range(N):
                        # (i,j) 와 (a,b) 가 K 이하인가? 가로길이 + 세로길이
                        dis = abs(a-i) + abs(b-j)
                        if dis < k and arr[a][b] == 1:
                            cnt += 1
                # 서비스 영역에 cnt개 만큼의 집이 있음
                if cnt * M >= cost:
                    # 여기에 해당하는 cnt중에 최대값 찾기
                    if cnt > max_cnt:
                        max_cnt = cnt
    return max_cnt

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = solve()
    # N이 최대 20이니까.. .K 는 최대 21
    # costs : k 별 운영 비용
    costs = [k*k +(k-1)*(k-1) for k in range(22)]
    print(f'#{tc} {result}')
#######################################################################
import sys
sys.stdin = open('input.txt','r')

def solve():
    # 도시의 모든 위치에서 서비스를 제공해 보기
    max_cnt = 0  #최대값 찾아야 하니 최소값으로 초기화
    for i in range(N):
        for j in range(N):
            for k in range(1, N+2):
                cnt = 0 #서비스 영역안에 있는 집의 개수
                # (i,j) 와 (a,b) 가 K 이하인가? 가로길이 + 세로길이
                for a,b in homes:
                    dis = abs(a-i) + abs(b-j)
                    if dis < k :
                        cnt += 1
                if cnt * M >= costs[k]: # 방범 비용이 손해가 아니면,
                    if cnt > max_cnt:
                        max_cnt = cnt
    return max_cnt

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    costs = [k*k +(k-1)*(k-1) for k in range(22)]
    # 집들의 위치를 homes 배열에 추가해서 방법 구역 포함여부를 확인할 때
    # 효율을 높임
    homes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                homes.append((i,j))

    result = solve()
    print(f'#{tc} {result}')
