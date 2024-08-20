
# BOJ 15657 N과 M(8) 실버 3

def dfs(level, lst):

    if level == M:
        print(*lst)
        return


    for i in range(N):
        if not lst:
            dfs(level+1, lst+[numbers[i]])
        else:
            if lst[-1] <= numbers[i]:
                dfs(level+1, lst+[numbers[i]])
            
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

dfs(0, [])