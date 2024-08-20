
def clarification(length):
    # 홀수 일 경우
    if real_n%2:
        for start in range(0, 2*(n-length)+2):
            left_string = sum(list(map(int, ticket[start : start+length])))
            right_string = sum(list(map(int, ticket[start+length : start+(2*length)])))
            if left_string == right_string:
                return True
    
    # 짝수 일 경우
    else:
        for start in range(0, 2*(n-length)+1):
            left_string = sum(list(map(int, ticket[start : start+length])))
            right_string = sum(list(map(int, ticket[start+length : start+(2*length)])))
            if left_string == right_string:
                return True
    
    return False

ticket = input().strip()
real_n = len(ticket)
n = real_n//2
result = 0
if n:
    for i in range(n, 0, -1):
        m = i * 2
        if clarification(i):
            result = m
            break

print(result)