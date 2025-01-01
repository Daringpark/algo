
# BOJ 1238 파티 (dijkstra, Heap Queue)
# 단방향 그래프, 그래프를 두 개 그릴 것 (가고 돌아오는 것으로)

import heapq
max_value = int(1e9)

def dijkstra(start, graph, n):
    # Possible Graph (except Zero Index)
    distance = [max_value] * (n+1)

    # settings
    distance[start] = 0
    pq = [(start, 0)]

    # Estimatation for dijkstra weight
    while pq:
        current_node, current_distance = heapq.heappop(pq)
        if current_distance > distance[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(pq, (next_node, new_distance))

    return distance

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    reverse_graph[e].append((s, w))

# distance from X or to X
dist_from_x = dijkstra(X, graph, N)
dist_to_x = dijkstra(X, reverse_graph, N)

max_weight = 0 
for i in range(1,  N+1):
    max_weight = max(max_weight, dist_from_x[i] + dist_to_x[i])

print(max_weight)