# 개수 세기

n = int(input())
A = list(map(int, input().split()))
number = int(input())
if number in A :
    print(A.count(number))
else : 
    print(0)

input()
print(input().split().count(input()))