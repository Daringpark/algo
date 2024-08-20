# 1330 두 수 비교하기
A, B = map(int, input().split())
if A >= -10000 and A <= 10000 and B >= -10000 and B <= 10000 :
    if A > B :
        print('>')
    elif A < B :
        print('<')
    else :
        print('==')