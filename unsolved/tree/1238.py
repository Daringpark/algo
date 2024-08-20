
# 백준 1238 파티

'''
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''


# dijkstra 문제
# 단방향 그래프이다.
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

print(graph)