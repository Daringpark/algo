


'''
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990

'''

N = int(input())
people = []
for _ in range(N):
    person = input().strip().split()
    person[1] = int(person[1])
    person[2] = int(person[2])
    person[3] = int(person[3])
    people.append(person)
people.sort(key = lambda x: (-x[3], -x[2], -x[1]))

print(people[0][0])
print(people[-1][0])