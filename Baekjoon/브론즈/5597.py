# 숙제 안낸 사람?
# 44ms , 108 B

Bag = list(range(1, 31))

for _ in range(28) :
    Bag.remove(int(input()))
print(f'{Bag[0]}\n{Bag[1]}')

# 두 개의 반복문으로 찾기; one-hot-encoding
# 44ms , 130 B

Bag = [0] * 30

for i in range(28) : 
    Bag[int(input()) -1] += 1
for j in range(30) :
    if Bag[j] != 1 :
        print(j + 1)
        
# O(N)