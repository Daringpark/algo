'''
3
CCP
CCP
PPC

'''

def candy(m):
    max_candy = 0

    # 사탕 교환
    for row in range(N):
        for col in range(N):
            # 오른쪽과 아래쪽 사탕과 교환
            # 위, 왼쪽은 이미 비교가 되거나 없는 행일 가능성(탐색방향이 col ++, row ++ 이기에)
            for dr, dc in [(0, 1), (1, 0)]:
                new_row = row + dr
                new_col = col + dc
                # 0 이상은 확인할 필요 없다. (좌표를 빼주지 않기에)
                if new_row < N and new_col < N:
                    # 바꿔준다.
                    m[row][col], m[new_row][new_col] = m[new_row][new_col], m[row][col]

                    # 연속 부분의 최대 길이 계산
                    for x in range(N):
                        count_row = 1
                        count_col = 1
                        for y in range(1, N):
                            if m[x][y] == m[x][y - 1]:
                                count_row += 1
                            else:
                                count_row = 1
                            if m[y][x] == m[y - 1][x]:
                                count_col += 1
                            else:
                                count_col = 1
                            max_candy = max(max_candy, count_row, count_col)

                    # 다시 사탕 교환 return (백트래킹)
                    m[row][col], m[new_row][new_col] = m[new_row][new_col], m[row][col]

    return max_candy

N = int(input())
matrix = [list(input()) for _ in range(N)]

# 출력단
print(candy(matrix))
