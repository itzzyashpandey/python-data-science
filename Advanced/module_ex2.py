from random import random
from random import randint , choice , shuffle , choices

val= random()
print(val)

for i in range(10):
    cal= randint(1,10)
    print(cal, end=' ')

num=[]
for i in range(10):
    num.append(randint(1,1000))
print("\n", num)    

animals=['🐯','🐷','😺','🦊','🦍','🐔','🐍','🐬','🐳','🐒','🐰','🐸','🐐']

sel_anl=choice(animals)
print(f"selected animals: {sel_anl} ")

sel_3_anl=choices(animals,k=3)
print(f'selected 3 animals: {" ".join(sel_3_anl)}')

shuffle(animals)
print(f'shuffle animals:   {"".join(animals)}')