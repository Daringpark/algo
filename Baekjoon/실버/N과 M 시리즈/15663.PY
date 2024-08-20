
N, M = map(int, input().split())
numbers = [map(int, input().split())]
visited = [0] * N
numbers.sort()

history = []
def dfs(level, lst):

    if level == M:
        if lst not in history:
            history.append(lst)
        print(history)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(level+1, lst + [numbers[i]])
            visited[i] = 0

dfs(0, [])
history.sort
history = list(set(history))
for result in history:
    print(*result)