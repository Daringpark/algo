# BOJ 13335 트럭 실버 1 

import sys
input = sys.stdin.readline
from collections import deque

# N은 다리를 건너는 트럭 개수, W는 다리의 길이, L은 다리의 하중을 나타낸다.
N, W, L = map(int, input().split())
Trucks = deque(map(int, input().split())) # 한 트럭의 무게는 10을 넘지 않는다.



Bridge = [0] * W
Completed = []
turn = 0
