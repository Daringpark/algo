# 펠린드롬 확인, 속도 40ms
word = input()
back_word = word[::-1] # slicing
if word == back_word :
    print(1)
else :
    print(0)