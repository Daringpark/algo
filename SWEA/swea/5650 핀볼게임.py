



T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # N은 최소 5, 최대 100, 웜홀은 6~10으로 주어진다. 블랙홀은 -1
    # 게임판에 웜홀, 블랙홀이 존재하지 않는 경우도 있다.
    # 웜홀에 들어갈 경우, 진행 방향은 그대로




    # 게임에서 얻을 수 있는 최대값을 구하라
    print(f'#{tc} ')