
# 버거 1, 사이드 1, 음료 1 선택시 < 10% 할인 적용
# 버거 개수 B, 사이드 C, 음료수 D

# 최대 1000개
B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
sodas = list(map(int, input().split()))

# 할인이 적용되기 전 == 그냥 sum값
before_sale = (sum(burgers) + sum(sides) + sum(sodas))
print(before_sale)

burgers.sort()
sides.sort()
sodas.sort()

after_sale = 0
while burgers and sides and sodas:
    b = burgers.pop()
    c = sides.pop()
    d = sodas.pop()
    after_sale += int((b+c+d) * 0.9)

after_sale += (sum(burgers) + sum(sides) + sum(sodas))
print(after_sale)