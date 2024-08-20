from collections import deque
N = int(input())
Balloons = deque(enumerate(map(int, input().split())))
poped = deque()
while Balloons:
    idx, amount = Balloons.popleft() # 값을 받아온다.
    poped.append(idx+1)
    if amount > 0: # 양수의 경우
        Balloons.rotate(-(amount-1))
    elif amount < 0:
        Balloons.rotate(-amount)
print(' '.join(map(str, poped)))

