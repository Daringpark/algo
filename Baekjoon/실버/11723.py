import sys
sys.stdin = open('11723.txt')

import sys # 59% 시간 초과
import copy

import sys
input = sys.stdin.readline
# N = int(input())
# S = set()
# all_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20} # 이렇게 불러오는 것 보다
# range(1,21) 이 오히려 더 빠르다.

# def solve():
#     global S
#     for _ in range(N):
#         command = input().split()
#         if len(command) == 2: # len method를 돌면서 시간 초과가 날 가능성이 매우 높음, 따라서
#                               # input.split을 받았으면 그냥 [0] 인덱스를 사용해서 확인하는게 더 빠르다.
#             amount = int(command[-1])
#             if command[0] == 'add' and amount not in S:
#                 S.add(amount)
#             elif command[0] == 'remove' and amount in S:
#                 S.remove(amount)
#             elif command[0] == 'check':
#                 if amount not in S:
#                     print(0)
#                 else:
#                     print(1)
#             elif command[0] == 'toggle':
#                 if amount not in S:
#                     S.add(amount)
#                 else:
#                     S.remove(amount)
#         else:
#             if command[0] == 'all':
#                 S = copy.deepcopy(all_set)
#             else:
#                 S = set()
# solve()


# 수정한 3400ms 정도의 코드
S = set()
M = int(input())
# M개의 연산 입력 및 처리
for _ in range(M):
    operation = input().split()  # 연산 입력
    if operation[0] == 'add':
        S.add(int(operation[1]))
    elif operation[0] == 'remove':
        x = int(operation[1])
        if x in S:
            S.remove(x)
    elif operation[0] == 'check':
        x = int(operation[1])
        if x in S:
            print(1)
        else:
            print(0)
    elif operation[0] == 'toggle':
        x = int(operation[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif operation[0] == 'all':
        S = set(range(1, 21)) # 이렇게 만드는게 더 빨랐다.
    elif operation[0] == 'empty':
        S = set()

