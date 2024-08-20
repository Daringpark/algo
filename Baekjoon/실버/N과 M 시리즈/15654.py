def per(n, lst):
    if n == M:
        print(*lst)
        return
    
    for number in numbers:
        if number not in lst:
            per(n+1, lst + [number])
    
# 1~8로 구성되어 있다.
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
per(0, [])