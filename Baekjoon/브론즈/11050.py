# 11050번 이항 계수 1 44ms
N, K = map(int, input().split())

mother_list = []
son_list = []
res = 1
for i in range(K) :
    mother_list.append(int(N - i))
    son_list.append(int(i + 1))
    res = res * (mother_list[i] / son_list[i])
print(int(res))

# combination의 메인 컨셉 // 40ms
# def f(n):
#     if n == 0:
#         return 1
#     return n * f(n-1)
# n, m = map(int, input().split())
# print(f(n)//f(n-m)//f(m))