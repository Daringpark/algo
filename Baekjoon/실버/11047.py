import sys
sys.stdin = open('11047_input.txt', 'r')

N, K = map(int, input().split())
money = []
for i in range(N) :
    money.append(int(input()))

for i in range(N) : # sort array
    for j in range(i+1, N) :
        if money[i] < money[j] :
            money[i], money[j] = money[j], money[i]

res = 0
for coin in money :

    count = K // coin # 몫을 구하기

    K -= count * coin # 몫과 나머지를 빼서 K 갱신
    res += count
print(res)