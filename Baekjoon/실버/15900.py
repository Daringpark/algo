
# BOJ 15900 나무 탈출 실버 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
# N <= 500000
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
distance = [0 for _ in range(N+1)] # 0이면 자신이 부모 노드

# 1. graph making
for _ in range(N-1):
    s, e = map(int, input().split())

    if e not in graph[s]:
        graph[s].append(e)

    if s not in graph[e]:
        graph[e].append(s)

# 2. main function DFS (stack -> recursive)
def dfs(node):
    visited[node] = 1
    for new in graph[node]:
        if not visited[new]:
            distance[new] = distance[node] + 1
            dfs(new)
dfs(1)

# 3. distance -> result
result = 0
for i in range(2, N+1): # 2~N까지
    if len(graph[i]) == 1: # 리프노드는 위로 올라가는 것 밖에 없음
        result += distance[i]

# 4. 출력단
if result%2:
    print('Yes')
else:
    print('No')
# 1 W, 2 L, 4 L
 
'''
8
8 1
1 4
7 4
6 4
6 5
1 3
2 3

  1
3 4 8(4)
2(1) 7(2) 6
  5(3)

'''

'''
8
1 2
6 2
3 2
3 7
4 3
8 4
4 5
'''