# 4796번 캠핑 ## 44ms
import sys
input = sys.stdin.readline

cnt = 1
while True :
    try :
        L, P, V = map(int, input().split())
        res = V%P 
        N = V//P

        if res > L:

            result = (N + 1) * L
            print(f'Case {cnt}: {result}')
        elif res <= L :
            
            result = N * L + res
            print(f'Case {cnt}: {result}')

        cnt += 1
    except ZeroDivisionError:
        break