# 직각삼각형 만들기

while True :
    lis = list(map(int, input().split()))
    lis = sorted(lis)
    if lis[0] != 0 :
        if lis[0]**2 + lis[1]**2 == lis[2]**2 :
            print('right')
        else :
            print('wrong')
    else :
        break

# 다른 분 풀이 :
# 입력 조건이 0 이상의 양의 정수라고 하였기에 성립

while True:
  a=list(map(int,input().split()))
  if a[0]==0:break # sort() 
  a=sorted(a)
  print('right' if a[0]**2+a[1]**2==a[2]**2 else 'wrong')