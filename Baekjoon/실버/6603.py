
def dfs(level, start, lst):

    if level == 6:
        print(*lst)
        return


    for i in range(start, numbers[0]):
        dfs(level+1, i+1, lst + [numbers[i+1]])

numbers = list(map(int, input().split()))
while numbers[0] != 0:

    pool = numbers[1:]

    dfs(0, 0, [])

    print()
    numbers = list(map(int, input().split()))