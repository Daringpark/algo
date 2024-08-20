def solve(n, lst):

    if n == K:
        print(*lst)
        return
    
    for i in range(N):
        solve(n+1, lst + [numbers[i]])

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

solve(0, [])