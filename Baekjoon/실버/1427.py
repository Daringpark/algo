
# BOJ 1427 소트인사이드
# 문자열 정렬 문제

N = list(input())
N.sort(reverse=True)

result = ''
for n in N:
    result += n
print(result)