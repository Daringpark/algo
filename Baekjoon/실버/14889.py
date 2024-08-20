
def back(n, lstA, lstB): # 0 ~ N-1까지 
    global min_value
    if len(lstA) > N//2 or len(lstB) > N//2:
        return
    
    if n == N:
        if len(lstA) == len(lstB): # N//2 로 같아질 때,
            sum_A = sum_B = 0
            for i in range(N//2):
                for j in range(N//2):
                    sum_A += Matrix[lstA[i]][lstA[j]]
                    sum_B += Matrix[lstB[i]][lstB[j]]
            min_value = min(min_value, abs(sum_A-sum_B))
        return
    
    back(n+1, lstA+[n], lstB) # n을 A extend
    back(n+1, lstA, lstB+[n]) # n을 B extend

N = int(input())
Matrix = [list(map(int, input().split())) for _ in range(N)]
min_value = 1e10
Team_A = []
Team_B = []
back(0, Team_A, Team_B) # depth, Team A, Team B가 N//2가 될 때 선수들이 다 정해진다.
print(min_value)