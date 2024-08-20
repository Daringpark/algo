
def per_round(lstA, lstB):

    for k in range(4, 0, -1):
        # 4 3 2 1을 확인
        if lstA[k] > lstB[k]:
            return 'A'
        elif lstA[k] < lstB[k]:
            return 'B'
        
        # 드로우
        if k == 1:
            return 'D'

# 라운드 수
N = int(input())

for round in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_count = [0] * 6
    B_count = [0] * 6
    for a in range(1, A[0]+1):
        A_count[A[a]] += 1
    for b in range(1, B[0]+1):
        B_count[B[b]] += 1

    print(per_round(A_count, B_count))


# 별 동그라미 네모 세모 == 4 3 2 1
# 승자가 A, B; 무승부 D
    