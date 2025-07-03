
### 택배 상자 꺼내기
import math

# 실제 매트릭스를 구현할 필요 없이 수식으로 풀 수 있을 것 같다.
def solution(n, w, num):
    pos_y = math.ceil(num / w)
    pos_direction = pos_y % 2 # 0 : left, 1 : right
    pos_x = num % w if num % w !=0 else w
    col = pos_x if pos_direction else w - pos_x + 1 
    
    # num pos
    print(col)
    answer = 0
    for l in range(pos_y, math.ceil(n / w) + 1):
        direction_check = l % 2
        if direction_check:
            box_num = (l - 1) * w + col 
        else:
            box_num = l * w - col + 1

        if box_num <= n:
            answer += 1
            # print(box_num, n)
    
    return answer

"""
다른 분들 풀이
def solution(n, w, num):
    m1 = num%(w*2)
    m2 = ((w*2+1) - m1)%(w*2)
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))

이렇게 쉽게 계산할 수 있구나
메모지에 수식을 정리해보자.
"""