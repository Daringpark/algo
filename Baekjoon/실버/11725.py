
# 백준 11725 트리의 부모 찾기
from collections import deque

# 트리의 루트는 1

N = int(input())
graph = [[] for _ in range(N+1)]
# 1. 그래프 그리기
for _ in range(N-1):

    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 2. 부모 찾기 (부모 리스트 만들어주기)
parent = [0] * (N+1)
queue = deque()
queue.append(1) # 1의 부모 노드는 필요 없음.

while queue:
    node = queue.popleft()

    for n in graph[node]: # 자식 노드 꺼내주기
        if not parent[n]: # 자식 노드의 부모가 정해지지 않았을 때
            parent[n] = node # 자식 노드의 부모 리스트에 채워주기 BFS
            queue.append(n) # 자식노드 큐 넣어주기

# 3. 문자열 join으로 출력하기
result = '\n'.join(map(str, parent[2:]))
print(result)