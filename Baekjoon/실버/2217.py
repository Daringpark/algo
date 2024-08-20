# N = int(input())

# ropes = []
# for i in range(N):
#     ropes.append(int(input()))
# ropes.sort()
# # print(ropes)

# # x = weight/n
# # max_value = ropes[0] # 이거 이상으로 나눠서 들 수 있는가
# result = []
# for x in ropes:
#     result.append(x*N)
#     N -= 1
# print(max(result))

N = int(input())

ropes = []
for i in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)
# print(ropes)
# x = weight/n
max_value = ropes[0]
idx = 1
while idx < N:
    if max_value < ropes[idx]*(idx+1):
        max_value = ropes[idx]*(idx+1)
    idx += 1

print(max_value)



