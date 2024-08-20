import heapq
import sys
input = sys.stdin.readline
# sys.stdout = open('output.txt', "w")

N = int(input())
numbers = []

for i in range(N):
    number = int(input())
    
    if number:
        heapq.heappush(numbers, number)
    else:
        if numbers:
            item = heapq.heappop(numbers)
            print(item)
        else:
            print(0)