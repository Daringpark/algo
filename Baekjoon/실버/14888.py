# 14888 연산자 끼워넣기 
def back(n, result, lstop):
    global max_value, min_value
    if min_value < -1e8 or max_value > 1e8: # 중간 결과 예외 처리
        return

    if n == N: # 끝까지 뽑았을 때,
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return

    # 아래는 어떤 요소를 가져왔는지를 받는다.
    if lstop[0] > 0: # 더하기
        lstop[0] -= 1
        back(n+1, result+numbers[n], lstop)
        lstop[0] += 1
    if lstop[1] > 0: # 빼기
        lstop[1] -= 1
        back(n+1, result-numbers[n], lstop)
        lstop[1] += 1
    if lstop[2] > 0: # 곱하기
        lstop[2] -= 1
        back(n+1, result*numbers[n], lstop)
        lstop[2] += 1
    if lstop[3] > 0: # 나누기
        lstop[3] -= 1
        back(n+1, int(result/numbers[n]), lstop)
        lstop[3] += 1

N = int(input()) # N을 기준으로 아래 값을 받는다.
numbers = list(map(int, input().split()))
oper = list(map(int, input().split())) # N-1 개가 들어갈 것 # 최대 11
min_value = 1e10 # 범위 설정 잘못 10억 이상 -10억 이하
max_value = -1e10
back(1, numbers[0], oper) # n = 0을 시작으로부터 lst의 첫번째 값을 취한다.
print(max_value)
print(min_value)