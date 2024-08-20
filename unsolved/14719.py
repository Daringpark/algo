
# BOJ 14719 빗물 골드 5
# 구현, 풀어볼 만한 시뮬레이션 구현 문제


import sys
sys.stdin = open('14719_input.txt')


H, W = map(int, input().split())
RAIN_MAP = list(map(int, input().split()))
print(RAIN_MAP)

'''
while문을 돌리면서 i = 0 부터
i = 0 완전 탐색할 예정
rain = 0 누적 빗물양 << return 할 값

while i != W:
0 초과인 스타트 지점을 처음 받고,
if rain_map[i] > 0:
start = rain_map[i] # 값
start_point = i # 좌표
스타트 지점보다 더 큰 지점을 받아서(0 초과인) 스타트 지점으로 받고,
elif rain_map[i] != 0 and start_point <= rain_map[i]:
end = rain_map[i] # 값
end_point = i # 좌표
rain += min([start, end])-rain_map[i] for i in range(start_point+1, end_point)
+ 엔드와 스타트지점의 최소값을 각 스타트 지점+1인 지점과 엔드지점-1인 지점까지의 사이값들을 총 합에 추가해준다.
이 지점보다 같거나 큰 값을 받으면, 엔드 지점으로 받는다.
++ 매 위치마다 빗물양을 추가해준다?
- 스타트 지점이 제일 크고, 엔드 지점이 작을때 스타트 지점에서 빗물을 재게되면 값이 다름.
- 스타트 지점이 작고, 엔드 지점이 작을 때 오케이

빗물을 다 쟀으면, 새로운 스타트 지점을 받는다.
start = end; start값은 제일 마지막의 닫는 지점에서 새로 정해진다. 
start_point = i+1 (for문을 돌고나서 i = endpoint - 1) # 닫으면서 새로운 스타트 포인트
end_point 는 start_point와 똑같이 가져간다.

i += 1 while문의 제일 마지막에 += 1
i == W가 되면, break


'''

i = 0
rain = 0

while i != W:
    start = 0
    if start or RAIN_MAP[i] > 0:
        start = RAIN_MAP[i]
        start_point = i
    elif RAIN_MAP[i] != 0 and start_point <= RAIN_MAP[i]:
        end = RAIN_MAP[i]
        end_point = i
        rain += (min([start,end]) - RAIN_MAP[i] for i in range(start_point+1, end_point))
        start = end
        start_point = i+1
    
    print(start_point, end_point)
    i += 1
    print(i)