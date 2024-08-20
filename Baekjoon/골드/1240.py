
# 시간 제한 2초, N* M = 1e6
import sys
from collections import deque
input = sys.stdin.readline

# 어차피 M번만큼 초기화 해줄꺼, 함수에서 초기화하자.
def bfs(start, end):

    visited = [0 for _ in range(N+1)]
    # length를 담아줄 예정
    # 초기는 1 체크 이후에
    visited[start] = 1
    
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for new_node, length in graph[node]:
            if not visited[new_node]:
                visited[new_node] = visited[node] + length
                queue.append(new_node)

    return visited[e]-1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)] # 0 ~ N까지

# N-1개만큼 그래프 그리기에 들어간다. 무향 그래프
for _ in range(N-1):
    s, e, l = map(int, input().split())
    graph[s].append((e, l))
    graph[e].append((s, l))

# 알고 싶은 갯수
for _ in range(M):
    s, e = map(int, input().split())

    print(bfs(s, e))