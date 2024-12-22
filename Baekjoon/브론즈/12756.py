aAttack, aHealth = map(int, input().split())
bAttack, bHealth = map(int, input().split())

flag = True

while flag:
    aHealth -= bAttack
    bHealth -= aAttack

    if aHealth <= 0 and bHealth <= 0:
        print("DRAW")
        flag = False
    elif aHealth <= 0:
        print("PLAYER B")
        flag = False
    elif bHealth <=0:
        print("PLAYER A")
        flag = False