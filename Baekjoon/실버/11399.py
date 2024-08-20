import sys
sys.stdin = open('11399_input.txt')

def solve(n): # n-1까지 순회
    global memo
    for i in range(1, n):
        if i == 1:
            memo[0] = A[0]
            memo[1] = memo[0] + A[1]
        elif i >= 2:
            memo[i] = memo[i-1] + A[i]

    if n == 1: time = A[0]
    if n >= 2:
        time = sum(memo[-2::-1]) + memo[-1]
    return time

N = int(input())
A = list(map(int, input().split()))
A.sort()
memo = [0] * N

print(solve(N))