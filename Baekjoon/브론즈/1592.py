# N, M, L = 5, 3, 2
N, M, L = map(int, input().split())
cnt = 0
pos = 0
real = [i for i in range(1, N+1)]
count_list = [0]*N
count_list[pos] = 1
while M not in count_list: # 리스트 안에 M이 있으면 종료
    if count_list[pos]%2:
        pos = (pos+L)%N
    else:
        pos = (pos-L)%N
        # if pos-L >= 0:
        #
        # else:
    count_list[pos] += 1
    cnt += 1
print(cnt)