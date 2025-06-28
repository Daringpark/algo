def mod_pow(a, b, c):
    if b == 0:
        return 1  # a^0 == 1
    half = mod_pow(a, b // 2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c
    
A, B, C = map(int, input().split())
print(mod_pow(A, B, C))