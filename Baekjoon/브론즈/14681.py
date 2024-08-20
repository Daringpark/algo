# 14681 사분면 고르기

x = int(input())
y = int(input())

if x > 0 and x <= 1000 :
    if y > 0 and y <= 1000 :
        print('1')
    elif y < 0 and y >= -1000 :
        print('4')
elif x < 0 and x >= -1000 :
    if y > 0 and y <= 1000 :
        print('2')
    elif y < 0 and y >= -1000 :
        print('3')