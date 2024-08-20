# 윤년 계산기
number = int(input())
result = 0

if number >= 1 and number <= 4000 :
    if number % 4 == 0 :
        if number % 100 != 0 :
            result = 1
        elif number % 400 == 0 :
            result = 1
        else :
            result = 0
print(result)

# 윤년 계산기 수정 , 논리 연산자 사용 (연산속도 동일, 코드 길이 --)
number = int(input())
result = 0

if number >= 1 and number <= 4000 :
    if number % 4 == 0 :
        if number % 100 != 0 or number % 400 == 0 :
            result = 1
        else :
            result = 0
print(result)
# Hard Logic 구현을 깔끔하게 하는 방법