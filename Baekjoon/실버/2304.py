"""
6
2 4
11 4
15 8
5 3
8 10
13 6
"""

# 2304 창고 다각형
N = int(input())
Boxes = [list(map(int, input().split())) for _ in range(N)]
Boxes.sort()

# 가장 높은 기둥의 인덱스와 기둥의 높이
i = 0
max_h = 0
for box in Boxes:
    if box[1] > max_h:
        max_h = box[1]
        idx = i
    i += 1

area = 0
# 왼쪽 계산
curr_h = Boxes[0][1]
for i in range(idx):
    if curr_h < Boxes[i+1][1]:
        area += curr_h * (Boxes[i+1][0] - Boxes[i][0])
        curr_h = Boxes[i+1][1]
    else:
        area += curr_h * (Boxes[i+1][0] - Boxes[i][0])

# 오른쪽 계산
curr_h = Boxes[-1][1]
for i in range(N-1, idx, -1):
    if curr_h < Boxes[i-1][1]:
        area += curr_h * (Boxes[i][0] - Boxes[i-1][0])
        curr_h = Boxes[i-1][1]
    else:
        area += curr_h * (Boxes[i][0] - Boxes[i-1][0])

print(area + max_h)