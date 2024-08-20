
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [0 for _ in range(N+1)]
    distance_list = [0 for _ in range(N+1)]
    queue = deque([1])
    visited[1] = 1

    while queue:
        node = queue.popleft()
        for new_node, length in graph[node]:
            if not visited[new_node]:
                visited[new_node] = 1
                distance_list[new_node] = distance_list[node] + length
                queue.append(new_node)

    return max(distance_list)

# 방은 1부터 N까지의 번호가 있다.
N = int(input())
# 1,2,3,4
graph = [[] for _ in range(N+1)]

# 입구에서 가장 먼 방으로 가려고 한다.
for _ in range(N-1):
    s, e, l = map(int, input().split())
    graph[s].append((e, l))
    graph[e].append((s, l))

print(bfs())

'''
6
1 2 1
2 3 2
2 4 4
3 5 5
2 6 1

'''