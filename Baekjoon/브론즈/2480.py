# 주사위 3개 던지기

lis = list(map(int, input().split()))
lis = sorted(lis)

if lis.count(lis[0]) == 3 :
    print(10000 + 1000 * lis[0])
elif lis.count(lis[0]) == 2 or lis.count(lis[1]) == 2 :
    print(1000 + lis[1] * 100)
else :
    print(lis[-1] * 100)
# else 반례가 따로 없음 두개의 컨디션 체크로도 충분함.
# 다른 분 풀이 : count() 사용하지 않고, 논리연산자 사용

a = list(map(int, input().split()))
a.sort()
if a[0]==a[2]:
    print(10000+a[0]*1000)
elif (a[0]==a[1]) or (a[1]==a[2]):
    print(1000+a[1]*100)
else:
    print(a[2]*100)