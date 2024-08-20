
# 백준 9934 완전 이진 트리
'''
2
2 1 3
LVR로 받았고, 이것을 트리 그래프를 출력으로 뽑아 내야한다. K = depth; level

# 출력단이
# root 3
# LR 1 5
# LR LR 0 2 4 6
# LR LR LR LR
# 이런식으로 출력되어야 한다
재귀 형식이 생각이 된다.
'''
# root_idx = 2**K//2-1

def down_to_depth(lst, level):

    V = len(lst)//2
    result[level].append(lst[V])

    # 재귀하지 않고, 빠져나온다. # L or R (leaf node)
    if len(lst) == 1:
        return
    
    # 0~V-1, 0~(V-1//2)-1, ... (L), (V) ,(R)
    down_to_depth(lst[:V], level+1)
    down_to_depth(lst[V+1:], level+1)

K = int(input())
LVR = list(map(int, input().split()))
result = [[] for _ in range(K)]

down_to_depth(LVR, 0)

# 0 -> level 1 -> ...
for k in result:
    print(*k)