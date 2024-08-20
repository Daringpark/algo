def per(n, lst):
    if n == M:
        print(*lst)
        return
    
    for number in numbers:
        per(n+1, lst + [number])
    
# 1~8로 구성되어 있다.
N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
per(0, [])