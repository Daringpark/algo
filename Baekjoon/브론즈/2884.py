# 2884 알람 시계
H , M = map(int, input().split())

if M < 45 and M >= 0 :
    M = 15 + M
    if H == 0 :
        H = 23
        print(H, M)
    elif H >= 0 and H <= 23 : 
        H -= 1
        print(H, M)
elif M >= 0 and M <= 60 and H >= 0 and H <= 23 :
    M -= 45
    print(H, M)

# 알람 시계 (코드 간결, 처리 속도 -)

H , M = map(int, input().split())
res = M - 45 # 남아 있는 분을 계산

if res < 0: # 45 미만인 경우,
    if H == 0: print(f"23 {60 + res}") # 시간이 0인 경우, 23 : 60 + res(음수)
    else: print(f"{H-1} {60 + res}") # 시간이 0이상인 경우, H-1 : 60 + res(음수)
else: # 45 이상일 경우
    print(f"{H} {res}") # 시간 변화는 없으니, H를 유지 : res(양수)