N = int(input()) # 노드의 갯수라고 이야기를 할 수 있겠다. range(1, N+1)
K = int(input()) # 그래프를 그리기 위해서 간선의 개수를 세준다.
visited = [0] * (N+1) # visited[1] 또한 1이기 때문에, 감염된 컴퓨터의 수를 세려면 x=visited.count(1) -1
graph = [[] for _ in range(N+1)]# 1 ~ N까지 + 0
for _ in range(K):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
stack = [1] # DFS로 풀어보고자 한다.
while stack:
    item = stack.pop()
    if not visited[item]:
        visited[item] = 1
        if graph[item]:
            stack.extend(graph[item]) # append를 하게 되면 [[], graph[item]]
print(visited.count(1)-1)