N, M = map(int, input().split())
Trees = list(map(int, input().split()))

# 이분 탐색 하기 위해 앞, 뒤 결정
start, end = 1, sum(Trees)
# log N 탐색하게되면 굉장히 빠르다.
while start <= end: # start가 더 커진다면 break
    mid = int((start+end)/2)
    res = 0 # 나무 절단 부분

    for tree in Trees:
        if tree > mid: # 커서 짤린다면 > 절단 부분으로 감
            res += tree - mid
    # 자른 나무들이 목표치와 같거나 높다면,
    if res >= M:
        start = mid + 1 # 절단 나무가 너무 많은 것, 시작점을 조정
    else:
        end = mid - 1
# end 값이 최대 높이가 된다. > start값은 그것보다 1 높은
print(end)

## 다른 분 풀이
import sys
input = sys.stdin.readline

def get_tree(trees, height):
    val = 0
    for tree in trees:
        if tree > height:
            val += tree - height
    return val

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
mid = 0
while start <= end:
    mid = (start + end) // 2
    cut_height = get_tree(trees, mid)

    if cut_height < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)