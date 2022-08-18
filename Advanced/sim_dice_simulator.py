import random


while True:
    input("enter to roll dice 🎲")
    roll=random.randint(1,6)
    print("you rolled a dice and got:🎲", roll)
    if roll==1:
        print("💀you loose💀 ")
        break
    elif roll==6:
        print("👑you winn👑 ")
        break
    else:
        print('keep rolling...')