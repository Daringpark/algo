'''
5
1 1 1 2 3
'''
# 1 1 | 1 2 | 3

N = 5
max_stack = N//2 + 1
carrot_box = [1,1,1,2,3]
# 3, 1, 1 || 2
# 1, 2, 2 || 1
## << 최소화
# 2, 1, 2 || 1
# 2, 2, 1 || 1
# permutation with minimum size

'''
만약에, 4P3, max_size = 3 , min_size = 1
min_size <= len(box) <= max_size
'''
