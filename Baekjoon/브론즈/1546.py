# 1546번 평균
T = int(input())
num_list = list(map(int, input().split()))
new_list = []

for number in num_list :
    new_list.append(number/max(num_list) * 100)
print(sum(new_list)/T)