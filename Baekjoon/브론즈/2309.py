# Q2. 난쟁이 찾기 (for range())
num_list = []

for i in range(9) :
    number = int(input())
    num_list.append(number)
num_list.sort()

end = 0 # flag
for i in range(9) :
    if end == 1 :
        break
    for j in range(9) :
        if num_list[j] == num_list[i] :
            continue
        elif sum(num_list) - (num_list[i] + num_list[j]) == 100 :
            le = num_list[j]
            num_list.remove(num_list[i])
            num_list.remove(le)
            end = 1
            break
print('\n'.join(map(str, num_list)))