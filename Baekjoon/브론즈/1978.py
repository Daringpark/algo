# 1978번 소수 찾기
T = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in lst :
    num_list = []
    for j in range(1, i+1) :
        if i % j == 0 :
            num_list.append(str(j))
    # print(num_list)
    if len(num_list) == 2 :
        cnt += 1
print(cnt)