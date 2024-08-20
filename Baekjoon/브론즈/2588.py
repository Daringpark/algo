# 곱셈
A = int(input())
B = int(input())

B_3 = B//100
B_2 = (B%100)//10
B_1 = (B%100)%10

print(f'{A*B_1}\n{A*B_2}\n{A*B_3}\n{A*B}\n')