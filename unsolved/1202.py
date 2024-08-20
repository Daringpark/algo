import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# N = 보석의 개수
# K = 가방의 개수
jewel = []
for i in range(N):
    jewel.append(list(map(int, input().split()))) # 무게와 가격
bags = []
for i in range(K):
    bags.append(int(input()))
# Quick sort를 써야할 것 같음 (NlogN).
# 일반 정렬은 시간이 오래걸릴 것 같고
# list에서 sort method 이후에 queue 전환해도 상관 없긴 할 듯
# O(NK)이면 9 * 10**10
    
# 뭔가 가방 무게랑 매칭이 안될 수도 있음
# 가치를 기준으로 하는게 아니라 일단 가방이랑 무게랑 맞추고, 그 중에서 가치가 가장 높은 것을 뽑는다.
jewel.sort(key = lambda x: (-x[0], -x[1]))
bags.sort(reverse=True) # 얘까지는 오케이
bags = deque(bags)
result = 0
for item in bags: # K
    # taken = deque() # popleft안해도 됨
    taken = []
    spliter = 0 # N
    # O(N*K) 이미 시간초과가 날 것
    n = len(jewel)
    while spliter <= n:
        if item >= jewel[spliter][0]:
            taken.extend(jewel[spliter:])
            break
        else:
            spliter += 1
    taken.sort(key = lambda x: x[1]) # 값 어치를 기준으로 재정렬
    jew = taken.pop()
    idx = jewel.index(jew)
    jewel.pop(idx)
    result += jew[1]
print(result)




# print(jewel, bags)


'''
5 2
5 10
100 100
20 100
40 100
5 30
50
11
'''
