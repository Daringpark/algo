# Q3. 블랙잭 (random)
# import random
# T, sum_aim = map(int, input().split())
# num_list = list(map(int, input().split()))
# sum_list = []

# while True :
#     choice_numbers = random.sample(num_list, 3)
#     choice_numbers.sort()
#     if choice_numbers not in sum_list :
#         sum_list.append(choice_numbers)
#     if len(sum_list) == T*(T-1)*(T-2)/6 :
#         break 
# sum_list.sort()

# differ_list = []

# for numbers in sum_list :
#     sum_prod = sum(numbers) - sum_aim
#     differ_list.append(abs(sum_prod))

# if 0 in differ_list :
#     print(sum(sum_list[differ_list.index(0)]))
# else :
# # elif 0 not in differ_list :
#     print(sum(sum_list[differ_list.index(min(differ_list))]))

# 결과 : 시간 초과 (while문이 돌아갈 때, 시간 복잡도 ++)

T, sum_aim = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = []
zero_list = []

for i in range(T) :
    for j in range(i+1, T) :
        for k in range(j+1, T) :
            sum_element = num_list[i] + num_list[j] + num_list[k]
            if sum_element <= sum_aim :
                sum_list.append(sum_element)
                zero_list.append(sum_aim - sum_element)

if 0 not in zero_list :
    print(sum_list[zero_list.index(min(zero_list))])
else :
    print(sum_list[zero_list.index(0)])

# cards = list(map(int, input().split()))
# sum = []
# for i in range(N):
#     for j in range(i+1,N):
#         for k in range(j+1,N):
#             x = cards[i]+cards[j]+cards[k] 
#             if x <= M:
#                 sum.append( M-x )
            
   
# near_index = sum.index(min(sum))

# print(M-sum[near_index])