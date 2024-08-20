# 1181번 단어 정렬
# 900ms
T = input()
A = []
for i in range(int(T)) :
    A.append(input())
total = []
for i in range(1, 51) :
    lnth_list = []
    for j in A :
        if len(j) == i :
            lnth_list.append(j)
    lnth_list = list(set(lnth_list))
    lnth_list.sort()
    if len(lnth_list) >= 1 :
        total.extend(lnth_list)
print('\n'.join(total))

# 64ms
import sys
input = sys.stdin.readline

Nword = []
N = int(input())

for _ in range(N) :
    word = input().strip()
    Nword.append(word)
    
total = list(set(Nword))
total.sort()
total.sort(key = len)
print("\n".join(total))