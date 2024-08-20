# 2609번 최대공약수와 최소공배수
M, N = map(int, input().split())
num_list_1 = []
num_list_2 = []

for i in range(1, M+1) :
    if M % i == 0 :
        num_list_1.append((i))
# print(num_list_1)

for i in range(1, N+1) :
    if N % i == 0 :
        num_list_2.append((i))
# print(num_list_2)

ANB = set(num_list_1).intersection(set(num_list_2))
print(max(ANB))
print(num_list_1[-1]//max(ANB)*num_list_2[-1])