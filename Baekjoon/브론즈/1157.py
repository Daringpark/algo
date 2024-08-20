# 1157 단어공부

word = input().upper()
alpha = list(set(word))
count_list = []
for letter in alpha:
    count_list.append(word.count(letter))
if count_list.count(max(count_list)) >= 2:
    print('?')
else: print(alpha[(count_list.index(max(count_list)))])