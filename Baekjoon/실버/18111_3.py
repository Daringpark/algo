import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
mine = {}
for _ in range(n) :
    for i in list(map(int, input().split())) :
        if i in mine :
            mine[i] += 1
        else :
            mine[i] = 1

height = list(mine.keys())
mini = min(height)
maxi = max(height)

time = 1e9
top = 0
for h in range(mini, maxi + 1) : # h를 만들어야함 기준이 되는 층 : 입력된 최소 층에서 최대 층까지 완전탐색
    item = 0
    plus = 0
    for i, j in mine.items() : # 현재 층이 어떤가?
        if i > h : # 깎아서 아이템에 추가해야됨
            item += (i - h) * j # 몇칸을 깎아야하나?
        else : # 아이템에서 빼내서 추가해야됨
            plus += (h - i) * j
    
    if item + b < plus : # 내가 가진거보다 많이 추가해야되면 ?
        continue # 말이 안됨
    else :
        t = (item * 2) + plus
        if time >= t :
            time = t
            top = h

print(time, top)


# for i in range(M):
#     print(*matrix[i])

'''
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2

250 35
'''