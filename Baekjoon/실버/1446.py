import sys
input = sys.stdin.readline

def back(n, now, s):
    global min_value

    # 가지 치기
    if now > D or s > min_value: # 일방통행과 s가 작은 값보다 커져버린 경우
        return

    # 지금 위치가 딱 정확히 목표 지점까지 왔다면 갱신
    if now == D:
        min_value = min(min_value, s)
        return

    # 지금 위치는 목표는 아니지만, 우리가 취할 지름길을 다 정했다면
    if n == length:
        s += D - now
        if min_value > s:
            min_value = s
        return
    
    # 재귀 돌기
    start, end, value = short_list[n]
    if now > start:
        back(n+1, now, s)
        return
    res = start - now
    # 지름길 취하기
    if res >= 0:
        back(n+1, end, s + res + value)
        back(n+1, now, s)

# N = 12 이하 정수
N, D = map(int, input().split())
# 모든 위치는 10000보다 작은 음이 아닌 정수
# 길이는 10000보다 작은 자연수
short_list = []
for _ in range(N):
    s, e, v = map(int, input().split())
    if e - s > v: # 지름길이 되는 조건
        if e <= D: # 일방통행 조건
            short_list.append((s,e,v))
short_list.sort(key = lambda x : (x[0], x[2]))
min_value = 1e9
length = len(short_list)
back(0, 0, 0)
print(min_value)