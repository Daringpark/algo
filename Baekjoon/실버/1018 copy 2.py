import sys
sys.stdin  = open('1018.txt', 'r')


def min(a,b):
    return a if a<b else b

def max(a,b):
    return a if a>b else b

M, N = map(int, input().split())
Matrix = [list(map(str, input())) for _ in range(M)]


B_chess = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

W_chess = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# for i in range(8):
#     for j in range(8):
        # B_chess[i][j] = 'B'




min_cnt = 1e10
for i in range(M-7):
    for j in range(N-7):
        raw_chess = [[0]*8 for _ in range(8)]
        cnt = 0
        cnt_B = 0
        cnt_W = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # raw_chess[k-i][l-j] = Matrix[k][l]
                if Matrix[k][l] != W_chess[k-i][l-j]:
                    cnt_W += 1
                if Matrix[k][l] != B_chess[k-i][l-j]:
                    cnt_B += 1

        min_cnt=min(min_cnt,min(cnt_B,cnt_W))


print(min_cnt)