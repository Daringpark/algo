# 달팽이는 오르고 싶다 2869번 // 수식 만들기

A, B, V = map(int, input().split())
v = A - B
if v == 1 :
    print(V - A + 1)
else :
    if V % v != 0 :
        print(V // v - 1)
    else :
        print(V // v)
# 이거 아마 틀렸을 건데?

## 정답코드
A, B, H = map(int, input().split())

res = (H-A)//(A-B)

if (H-A)%(A-B) == 0 :
    print(res + 1)
else :
    print(res + 2)