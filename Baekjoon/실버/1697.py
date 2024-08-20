
from collections import deque

# 10만까지
visited = [0] * 100001
N, K = map(int, input().split()) # 시작점과 목표지점
visited[N] = 1

queue = deque()
queue.append(N)

while queue:
    num = queue.popleft()
    n1 = num - 1
    n2 = num + 1
    n3 = 2 * num

    if n1 >= 0:
        if visited[n1] >= visited[num] + 1 :
            visited[n1] = visited[num] + 1
            queue.append(n1)
        elif not visited[n1]:
            visited[n1] = visited[num] + 1
            queue.append(n1)

    if n2 <= 100000:
        if visited[n2] >= visited[num] + 1 :
            visited[n2] = visited[num] + 1
            queue.append(n2)
        elif not visited[n2]:
            visited[n2] = visited[num] + 1
            queue.append(n2)

    if n3 <= 100000:
        if visited[n3] >= visited[num] + 1 :
            visited[n3] = visited[num] + 1
            queue.append(n3)
        elif not visited[n3]:
            visited[n3] = visited[num] + 1
            queue.append(n3)

print(visited[K]-1)