N, K = 5,3
N, K = map(int, input().split())

queue = [i+1 for i in range(N)]
new_queue = []
pos = K - 1
while queue:
    if len(queue) > 1:
        pos = pos%len(queue)
        item = queue.pop(pos) # 사실상 팝이 강제적
        new_queue.append(item)
        pos += K-1
    else: new_queue.append(queue.pop())
print('<', end = '')
print(*new_queue, sep = ', ', end = '>')