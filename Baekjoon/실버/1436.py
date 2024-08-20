
N = int(input())
cnt = 0
for i in range(10000000):

    if i >= 666 :
        movie = str(i)
        if '666' in movie:
            cnt += 1

    if cnt == N:
        print(i)
        break