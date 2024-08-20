import sys
sys.stdin = open('switch.txt')


# light = 'YNYNYNYN'
# light = list(light)
import sys
input = sys.stdin.readline
light = list(input().strip()) # YYYYYY, YNYNYNYN
N = len(light) # N개의 전구 1부터 N까지 --> 0 ~ N-1까지
cnt = 0
while 'Y' in light:
    select_switch = light.index('Y')+1
    for i in range(1, N+1):
        if i%select_switch: # 배수일 때,
            pass
        else:
            if light[i - 1] == 'Y':
                light[i - 1] = 'N'
            else:
                light[i - 1] = 'Y'
    cnt += 1
print(cnt)