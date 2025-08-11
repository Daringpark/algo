import sys
input = sys.stdin.readline

### making prime number
primes = [1 for _ in range(1000001)] # range 2 <= 1000000
for i in range(2, 1000001):
    if primes[i]:
        for j in range(i*2, 1000001, i): # multiplication
            primes[j] = 0

### main
T = int(input())
for _ in range(T):
    partition = 0
    N = int(input())
    for num in range(2, N//2 + 1): # end-point : medium + 1
        if primes[num] and primes[N - num]:
            partition += 1
    print(partition)