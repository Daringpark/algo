import sys
sys.stdin = open('3060_input.txt')


def daycycle():
    demand = [0 for _ in range(6)]
    for i in range(6):
        demand[i] += memo[i] + memo[(i+1)%6] + memo[(i+3)%6] + memo[(i+5)%6]
        # print(demand[i])
    for i in range(6):
        memo[i] = demand[i]

T = int(input())
for tc in range(1, T+1):
    memo = [0] * 6
    food = int(input())
    table = list(map(int, input().split()))
    for i in range(6):
        memo[i] = table[i]
    cnt = 1
    while sum(memo) <= food:
        cnt += 1
        daycycle()
    print(cnt)