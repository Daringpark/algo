import sys
sys.stdin  = open('1018.txt', 'r')

def min(a,b):
    return a if a<b else b

M, N = map(int, input().split())
Matrix = [list(map(str, input())) for _ in range(M)]


chess_w=['W','B','W','B','W','B','W','B']
chess_b=['B','W','B','W','B','W','B','W']

def check(start,i,j):
    cnt=0
    for k in range(i, i+8):
        for l in range(j, j+8):
            if start: # Black
                if (k-i)%2==0 and Matrix[k][l]!=chess_b[l-j]:
                    cnt+=1
                if (k-i)%2==1 and Matrix[k][l]!=chess_w[l-j]:
                    cnt+=1
            else:
                if (k-i)%2==0 and Matrix[k][l]!=chess_w[l-j]:
                    cnt+=1
                if (k-i)%2==1 and Matrix[k][l]!=chess_b[l-j]:
                    cnt+=1
    return cnt


min_cnt = 1e10
for i in range(M-7):
    for j in range(N-7):
        cnt_BorW=min(check(True,i,j),check(False,i,j))
        min_cnt=min(min_cnt,cnt_BorW)


print(min_cnt)