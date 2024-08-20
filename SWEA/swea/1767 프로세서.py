'''
1
5
1 1 1 1 1
1 1 0 0 1
0 0 0 1 1
0 0 0 1 1
1 0 1 1 1

1,1 을 연결하지 않고,
(2,3) (3,3) 연결하는게 최대 연결 수, 3+3
: 6
'''



T = int(input())
for tc in range(1, T+1):
    
    N = int(input()) # cell N*N matrix
    matrix = [list(map(int, input().split())) for _ in range(N)]


    # 전선은 직선으로 밖에 연결이 되지 않는다.
    # 재귀를 돌려서 matrix를 변환해준다?    
    
    
    
    print(f'#{tc} ')