# 2시 시작
# 2시 45분 완 
import sys
sys.stdin = open('18870_input.txt')

def make_dict():
    pos = 0
    number_dict[new_numbers[0]] = 0
    # if N != 1:
    for i in range(1, N):
        number_dict.setdefault(new_numbers[i-1], False)
        if new_numbers[i-1] < new_numbers[i]:
            number_dict[new_numbers[i-1]] = pos
            pos += 1
        else: 
            number_dict[new_numbers[i-1]] = pos
    number_dict.setdefault(new_numbers[-1], False)
    if not number_dict[new_numbers[-1]]:
        number_dict[new_numbers[-1]] = pos
def solve():
    res = ''
    for num in numbers:
        res += str(number_dict[num])
        res += ' '
    res.strip()
    return res
N = int(input())
numbers = list(map(int, input().split())) # 이 순서대로 뽑아줘야 한다.
new_numbers = sorted(numbers) # 크기 비교를 위한 정렬 리스트 
number_dict = dict() # 해시를 이용해서 빠르게 좌표에 대한 값을 뽑아내기 위해서
make_dict()
print(solve())