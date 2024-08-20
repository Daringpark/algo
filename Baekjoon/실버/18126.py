
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(nod, length):
    global max_length
    # 리프 노드 접근은 잘못된건가?
    if not graph[nod]:
        if max_length < length:
            max_length = length
        return
    
    for node, new_length in graph[nod]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, length+new_length)
            visited[node] = 0

# 방은 1부터 N까지의 번호가 있다.
N = int(input())
# 1,2,3,4
graph = [[] for _ in range(N+1)]
# vistied = [0 for _ in range(N+1)]
# 입구에서 가장 먼 방으로 가려고 한다.
for _ in range(N-1):
    s, e, l = map(int, input().split())
    graph[s].append((e, l))
    graph[e].append((s, l))

max_length = 0
visited = [0 for _ in range(N+1)]
dfs(1, 0)

print(max_length)

'''
6
1 2 1
2 3 2
2 4 4
3 5 5
2 6 1

'''