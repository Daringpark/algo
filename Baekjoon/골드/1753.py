
# 1753 최단경로
import heapq as hq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = float("inf")
graph = {i: [] for i in range(1, V+1)}

distance = [INF] * (V + 1)
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
# print(graph)

# heap queue init
heap_queue = []
hq.heappush(heap_queue, (0, K))

# distance calculate
while heap_queue:
    dist, now = hq.heappop(heap_queue)

    if dist > distance[now]:
        continue

    for new_n, weight in graph[now]:
        new_dist = dist + weight
        if new_dist < distance[new_n]:
            distance[new_n] = new_dist
            hq.heappush(heap_queue, (new_dist, new_n))

# for loop print
for i in range(1, V+1):

    if not distance[i] == INF:
        print(distance[i])
    else:
        print("INF")
