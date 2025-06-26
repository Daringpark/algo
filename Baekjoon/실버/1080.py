
# 1080.py

n, m = map(int, input().split()) 
listA = [list(map(int, input())) for _ in range(n)]
listB = [list(map(int, input())) for _ in range(n)]

def check(row, col): # 뒤집기 함수
    for new_row in range(row, row+3):
        for new_col in range(col, col+3):
            if listA[new_row][new_col] == 0:
                listA[new_row][new_col] = 1
            else:
                listA[new_row][new_col] = 0

cnt = 0 # 카운트
if (n < 3 or m < 3) and listA != listB:
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                check(r, c)

if cnt != -1:
    if listA != listB: # A와 B가 같은지 확인
        cnt = -1
print(cnt)