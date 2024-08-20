
T = int(input())
for tc in range(1, T+1):
    t = input()
    cup, yolk, sugar, salt, flour = map(int, input().split())
    banana, jam, choco, walnut = map(int, input().split())
    '''
    8 8 4 1 9 = 16개 * 실수 x
    '''
    x = int(min(cup/8, yolk/8, sugar/4, salt/1, flour/9)*16)
    y = int(banana + jam//30 + choco//25 + walnut//10)
    '''
    바나나 - 1 : 1
    잼 - 30 : 1
    초코 - 25 : 1
    호두 - 10 : 1
    '''
    if x >= y :
        print(y)
    else:
        print(x)



'''
2

16 16 8 2 17
10 47 100 19

16 16 8 2 17
10 470 100 19
'''