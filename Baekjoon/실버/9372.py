
# BOJ 9372 상근이의 여행 
# 최소 스피닝 트리 (가중치가 같은 MST 최소 신장 트리 : 미니멈 스패닝 트리)

from collections import deque

def BFS(num):
    global cnt

    queue = deque()
    queue.append(num)
    visited[num] = 1
    
    while queue:
        item = queue.popleft()

        for s in graph[item]:
            if not visited[s]:
                visited[s] = 1
                queue.append(s)
                cnt += 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    visited = [0] * (N+1)
    cnt = 0
    # 1부터 N 노드까지 순회
    for i in range(1, N+1):
        BFS(i)
    print(cnt)