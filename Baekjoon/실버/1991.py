
def traversal(nod, order):
    global result
    LR = graph[nod]

    # VLR
    if order == 0:
        result += chr(nod+65)
        if LR[0] != -19:
            traversal(LR[0], order)
        if LR[1] != -19:
            traversal(LR[1], order)

    # LRV
    elif order == 1:
        if LR[0] != -19:
            traversal(LR[0], order)
        result += chr(nod+65)
        if LR[1] != -19:
            traversal(LR[1], order)

    # LRV
    elif order == 2:
        if LR[0] != -19:
            traversal(LR[0], order)
        if LR[1] != -19:
            traversal(LR[1], order)
        result += chr(nod+65)

# print(ord('A') - 65)
N = int(input())
graph = [0] * 26

for _ in range(N):
    node = input().split()
    graph[ord(node[0])-65] = [ord(node[1])-65, ord(node[2])-65]
# root는 항상 'A' == ord 65
root = 0
# print(graph)

for i in range(3):
    result = ''
    traversal(root, i)
    print(result)