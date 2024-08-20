# 15686 chicken delivery
def solve(num, dis, lst):
    global min_value
    if dis > len(chicken): # chicken의 길이만큼 돌아야하기 때문에
        return

    if num == M: # M개의 치킨집을 받았을 경우
        sum_distance = 0
        for row, col in house:
            distance = 1e8
            for i in range(len(lst)): # 취할 치킨집만 골라서
                if lst[i]:
                    r, c = chicken[i]
                    distance = min(distance, abs(row-r)+abs(col-c))
            sum_distance += distance
        min_value = min(min_value, sum_distance)
        return

    # 재귀
    solve(num+1, dis+1, lst+[1])
    solve(num, dis+1, lst+[0])

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)] # N 2500
# 치킨집 2의 개수는 13이랑 같거나 작지만, M보다 크거나 같다. (1 <= M <= 13)
min_value = 1e8
house, chicken = [], []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append([i, j])
        elif matrix[i][j] == 2:
            chicken.append([i, j])

solve(0,0, []) # 
print(min_value)