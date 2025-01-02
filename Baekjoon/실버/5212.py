def check(map):
    top, left, bottom, right = 0, C-1, 0, 0

    # forward row
    for i in range(R):
        if 'X' in map[i]:
            top = i
            break

    # backward row
    for i in range(R-1, -1, -1):
        if 'X' in map[i]:
            bottom = i
            break

    for i in range(top, bottom+1):
        for j in range(C):
            if map[i][j] == 'X':
                left = min(left, j)
                right = max(right, j)

    return top, left, bottom, right

R, C = map(int, input().split())
map = [input() for _ in range(R)]
changed_map = []
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Brute Force 10*10*4
for i in range(R):
    for j in range(C):
        # land searched
        count = 0
        if map[i][j] == 'X':
            for dr, dc in drdc:
                new_i = i + dr
                new_j = j + dc

                if (0 <= new_i < R) and (0 <= new_j < C):
                    if map[new_i][new_j] == '.':
                        count += 1
                else: # out of boundary
                    count += 1

        if count >= 3:
            changed_map.append((i, j))

# make them flood
if changed_map:
    for i, j in changed_map:
        map[i] = map[i][:j] + '.' + map[i][j+1:]

top, left, bottom, right = check(map)

for i in range(top, bottom+1):
    for j in range(left, right+1):
        print(map[i][j], end='')
    print()