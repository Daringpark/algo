# import sys
# input = sys.stdin.readline
vowel_list = ['a', 'e', 'i', 'o', 'u']

def dfs(level, start, res, vowel, consonant):

    if level == R and (vowel >= 1 and consonant >= 2):
        print(res)
        return

    for i in range(start, P):
        if not visited[i]:
            visited[i] = 1
            if alpha[i] in vowel_list:
                dfs(level+1, i+1, res+alpha[i], vowel + 1, consonant)
            else:
                dfs(level+1, i+1, res+alpha[i], vowel, consonant+1)
            visited[i] = 0

R, P = map(int, input().split())
alpha = list(input().strip().split())
alpha.sort()

visited = [0] * P
dfs(0, 0,'', 0, 0)