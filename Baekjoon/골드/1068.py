
# 시간 제한 2초
def find_leaf(node):
    global answer

    # 현재 노드에 연결된 다른 노드 탐색
    for next_node in graph[node]:
        # 재귀 사용
        find_leaf(next_node)

    # 현재 노드가 삭제한 노드이거나 현재 노드에 연결된 다른 노드가 없다면 해당 노드가 리프 노드
    if not graph[node]:
        answer += 1

# 노드 개수
N = int(input())
# 입력 받은 정보
tree = list(map(int, input().split()))

# 트리 구조 저장할 그래프
graph = [[] for _ in range(N)]
for node in range(N):
    p = tree[node]

    # 루트 노드 번호 찾기
    if p == -1:
        root = node
        continue

    graph[p].append(node)

# 삭제할 노드 번호
delete_node = int(input())
# 삭제할 노드 번호는 삭제해줌
graph[delete_node] = []

# 그래프에 저장되어 있는 삭제 노드 번호를 삭제 해 줌
for g in graph:
    if delete_node in g:
        g.remove(delete_node)

answer = 0
# 리프 노드 찾기
if root == delete_node:
    print(0)
else:
    find_leaf(root)
    print(answer)