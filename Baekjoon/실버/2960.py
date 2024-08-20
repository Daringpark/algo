
# 2960 에라토스테네스의 체
# 정수론 기본
# N <= 1000, K는 N보다 작음
N, K = map(int, input().split())

# 1. 2부터 N까지의 모든 정수를 적는다. prime number임을 표현하기 위해서 배열을 하나 더 만들기
main_table = list(range(2, N+1))
visited = [0] * (N+1) # 0,1까지 포함한 prime true, false

# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다!
# N 탐색, 조건을 활용해서 visited 처리와 프라임 넘버를 바꿔주자.
cnt = 0
for i in range(N-1):
    n = main_table[i]
    # 소수를 먼저 바꿔주고
    if not visited[n]:
        visited[n] = 1
        cnt += 1
    else:
        continue

    if cnt == K:
        print(n)
        break

    for k in range(n, N+1, n):
        if not visited[k]:
            visited[k] = 1
            cnt += 1
            if cnt == K:
                break

    if cnt == K:
        print(k)
        break