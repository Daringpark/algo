M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

def check(A, B):
    for k in range(N-1):
        for l in range(k+1, N):
            if (A[k] < A[l] and B[k] >= B[l]) or (A[k] > A[l] and B[k] <= B[l]) or (A[k] == A[l] and B[k] != B[l]):
                return 0

    return 1

result = 0
# combination M C 2
for i in range(M-1):
    for j in range(i+1, M):
        # A B C => (A, B), (A, C), (B, C)
        if check(matrix[i], matrix[j]):
            result += 1

print(result)