
# BOJ 1817 짐 챙기는 숌 실버 5
import sys
from collections import deque

N, W = map(int, input().split())

if N:
    books = deque(list(map(int, input().split())))
else:
    print(0)
    sys.exit()

box = 0
result = 0
while books:

    hand = books.popleft()
    box += hand
    
    if box > W:
        result += 1
        box = hand

if box:
    result += 1
print(result)