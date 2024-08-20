from collections import deque
import sys
input = sys.stdin.readline

# 정리된 풀이
# 입력
N = int(input())
graph = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    # BFS 탐색
    visited = [0]*(N+1)
    queue = deque([1]) # 시작은 1에서 시작
    while queue:
        x = queue.popleft()
        if x + graph[x-1] >= N: # level 바로 출력
            print(visited[x]+1)
            break
        for i in range(1, graph[x-1]+1): # 1 ~ 길이만큼 점프
            nx = x+i # 새로운 x로 도달할 지점
            if visited[nx] == 0:
                queue.append(nx) # 그 발판에도 값이 있으면 뛰어주는 큐로 인계
                visited[nx] = visited[x]+1 # 레벨링 ++
    else:
        print(-1)