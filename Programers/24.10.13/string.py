
# 문자열을 받을 때, n자로 정렬하고
# n자가 같다면, 사전순으로 배열한다.
def solution(strings, n):

    # lambda sort를 이용해 간단하게 구현할 수 있다.
    strings.sort(key= lambda x : (x[n], x))

    return strings
