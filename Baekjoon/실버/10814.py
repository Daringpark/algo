# 10814번 나이순 정렬
# import sys
# input = sys.stdin.readline

# N = int(input())
# PersonList = []
# for i in range(N) :
#     person = list(map(str, input().split()))
#     PersonList.append(person)

# for i in range(N) :
#     PersonList[i]
#     print(' '.join(PersonList[i]))
# 실패 // 가입한 순서대로가 아님 << sort로 풀이하는게 아니다.
# 그럼 어떻게? 딕셔너리 키와 밸류로. 나이는 key값을 받고, value로 사람 이름을 넣어준다. append 형식

#### 중요 !!!!!
import sys
input = sys.stdin.readline

N = int(input())
person_dictionary = {}

for i in range(N) :
    person_age , person_name = map(str, input().split())
    if person_age not in person_dictionary :
        person_dictionary[person_age] = [person_name]
    else :
        person_dictionary[person_age].append(person_name)

Age_key = list(person_dictionary.keys()) # key를 리스트로 저장
# print(Age_key)
for age in Age_key :

    for j in len(person_age[age].values()) :
        print(f'{age} ')
# {Age_key[age]}
# print(person_dictionary)
        





