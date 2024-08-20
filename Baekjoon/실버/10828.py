# 10828번 스택
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline

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