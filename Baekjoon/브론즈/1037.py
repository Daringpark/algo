# 1037번 : 약수
T = int(input())
num_list = sorted(list(map(int, input().split())))
print(min(num_list)*max(num_list))