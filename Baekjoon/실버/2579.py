
def upstairs(n):
    if n == 1:
        return stairs[0]

    jump_step = [stairs[0], stairs[1]]
    next_step = [stairs[0], stairs[0]+stairs[1]]

    while len(jump_step) <= N-1 or len(next_step) <= N-1:
        jump_step.append(max(jump_step[-2], next_step[-2])+ stairs[len(jump_step)])
        next_step.append(jump_step[len(next_step)-1] + stairs[len(next_step)])

    return max(jump_step[N-1], next_step[N-1])

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

print(upstairs(N))