
# 균형잡힌 세상은 [], ()가 잘맞는지 확인해야 함
import sys
input = sys.stdin.readline


def check():

    while True:
        sentence = input().rstrip()

        if sentence == '.':
            break

        # bracket storage
        stack = []
        bracket_dict = {")": "(", "]": "["}
        if sentence[-1] == '.':
            flag = True
        else:
            flag = False

        if flag:
            for letter in sentence:
                if letter in "([":
                    stack.append(letter)
                elif letter in ")]":
                    if stack and stack[-1] == bracket_dict[letter]:
                        stack.pop()
                    else:
                        flag = False
                        break
            if stack: # 앞 괄호만 있을 때
                flag = False

        if flag:
            print("yes")
        else:
            print("no")

check()