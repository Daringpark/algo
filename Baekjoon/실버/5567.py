from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(N+1)]
queue = deque()
for e in graph[1]:
    queue.append((1, e))
visited[1] = 1 # 1에서 시작, 3까지 세기

while queue:
    start, node = queue.popleft()
    if not visited[node]:
        for new_node in graph[node]:
            queue.append((node, new_node))
            visited[node] = visited[start] + 1

# Result : O(N) - 친구와 친구의 친구만 초대
count = 0
for i in range(N+1):
    if 1 < visited[i] <= 3:
        count += 1
print(count)