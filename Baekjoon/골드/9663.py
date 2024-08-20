
# 백준 9663 N-Queen

import time
start_time = time.time()

# 해당 행렬에서 대각선과 겹치는 열이 있나 체크
def check(level):
    for n in range(level):
        # 겹친다면, 그건 실패한 것 == 실패
        # 이 부분을 직접 확인하기에는 불필요.
        if abs(visited[level] - visited[n]) == level - n or (visited[n] == visited[level]):
            return 1
    # 다 돌았을 때 문제가 없다. == 성공
    return 0

def dfs(level):
    global cnt

    if level == N:
        cnt += 1
    
    # 아직 N 미만
    else:
        # 퀸 놓을 자리 보기
        for k in range(N):
            visited[level] = k
            # 다음 것 놓기 전에 검증하기
            if not check(level):
                dfs(level + 1)

N = int(input())
cnt = 0

visited = [0] * N
dfs(0)
print(cnt)
end_time = time.time()
exceution_time = end_time - start_time
print(exceution_time)