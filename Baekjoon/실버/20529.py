
def clear(per):
    idx = 0
    if per[0] == 'I':
        idx += 2**0
    if per[1] == 'N':
        idx += 2**1
    if per[2] == 'F':
        idx += 2**2
    if per[3] == 'P':
        idx += 2**3
    return idx

def compare(a, b):
    m = 0
    for i in range(4):
        if a[i] != b[i]:
            m += 1
    return m

def comb(level, start, lst):
    global minV

    if level == 3:
        m = compare(pool[lst[0]], pool[lst[1]]) + compare(pool[lst[2]], pool[lst[1]]) + compare(pool[lst[0]], pool[lst[2]])
        if minV > m:
            minV = m
        return

    for i in range(start, n):
        if i not in lst:
            comb(level + 1, i + 1, lst + [i])


T = int(input())
Index = ['ESTJ', 'ISTJ', 'ENTJ', 'INTJ', 'ESFJ', 'ISFJ', 'ENFJ', 'INFJ',
         'ESTP', 'ISTP', 'ENTP', 'INTP', 'ESFP', 'ISFP', 'ENFP', 'INFP']
for _ in range(T):

    minV = 12
    N = int(input())
    MBTI = list(input().split())
    
    counting = [0] * 16
    for item in MBTI:
        counting[clear(item)] += 1

    # flag = 1, 함수를 거칠 필요 없음
    flag= 0
    for i in range(16):
        if counting[i] >= 3:
            flag = 1
            minV = 0
            break

    if not flag:
        # 32 이하 pool
        pool = []
        for i in range(16):
            for _ in range(counting[i]):
                pool.append(Index[i])

        n = len(pool)
        comb(0, 0, [])

    print(minV)