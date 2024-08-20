import sys
input = sys.stdin.readline

def change(arr):
    result = [['O'] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 현재 위치가 폭탄 -> 본인 포함 자기 주변 바꾸기
            if arr[i][j] == 'O':
                for di, dj in dir:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        result[ni][nj] = '.'
    return result

# R, C : 격자 크기(1 <= R, C <= 200)
# N : 격차판 상태를 출력해야 하는 시간(1 <= N <= 200)
R, C, N = map(int, input().split())
# . : 빈 칸
# O : 폭탄
arr = [list(input()) for _ in range(R)]
dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
'''
1초 후 아무일도 X
폭탄은 설치된 후 3초 뒤에 폭발
- 폭발 시, 해당 칸은 빈칸이 되고, 인접 네 칸도 함께 빈 칸이 됨

1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
4. 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
5. 3과 4를 반복한다.

- K초에 폭탄이 있음 -> K+1초에 본인 기준 상하좌우 포함 5개 사라짐
- 약간 2초 단위로 하는 행위가 반복됨

'''

# 내가 풀고 싶었던 방향성이 이거였다.
# 결국 반복되는 구간이 생기고, matrix의 반복이 생기기에
# 해시로 극복? 혹은 T의 주기를 알아내는 방법이 필요했음
if N == 1:
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end = '')
        print()
elif N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print("O", end = '')
        print()
elif N % 4 == 3:
    arr = change(arr)
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end = '')
        print()
elif N % 4 == 1:
    arr = change(change(arr))
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end='')
        print()
