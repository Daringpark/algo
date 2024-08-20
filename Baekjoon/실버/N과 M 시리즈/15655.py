def solve(n, lst):

    if n == M:
        lst.sort()
        if lst not in hist:
            hist.append(lst)
            print(*lst)
            return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            solve(n+1, lst + [numbers[i]])
            visited[i] = 0

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * N
hist = []
solve(0, [])