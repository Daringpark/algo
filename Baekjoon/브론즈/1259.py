# 1259번 팰린드롬수
## 44ms
# word = None

while word != '0' : # 정지정지
    word = input()
    if word[::-1] == word and word != '0':
        print('yes')
    elif word == '0' :
        break
    else :
        print('no')