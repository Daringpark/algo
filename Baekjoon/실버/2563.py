# 2563번 색종이
import sys
input = sys.stdin.readline # 이거 추가해서 56ms

Test_case = int(input())
stack_list = []

for i in range(Test_case) :
    Order = list(map(str, input().split()))
    M = len(Order)

    if M >= 2 :
        stack_list.append(int(Order[1]))
    else :
        N = len(Order[0])
        if N >= 5 :
            if len(stack_list) == 0 :
                print(1)
            else :
                print(0)
        elif N >= 4 :
            print(len(stack_list))
        else :
            if Order[0] == 'top' :
                if len(stack_list) == 0 :
                    print(-1)
                else : 
                    print(stack_list[-1])
            else :
                if len(stack_list) == 0 :
                    print(-1)
                else : 
                    print(stack_list[-1])
                    stack_list.pop(-1)