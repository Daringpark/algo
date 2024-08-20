def solve():
    for i in range(9):
        for j in range(i+1, 9):
            if i != j:
                make_hundred = sum(numbers) - ((numbers[i] + numbers[j]))
            if make_hundred == 100:
                numbers.remove(numbers[i]) 
                numbers.remove(numbers[j-1]) # 감소하기 때문에
                return
numbers = [int(input()) for _ in range(9)]
solve()
for i in range(7):
    print(numbers[i])