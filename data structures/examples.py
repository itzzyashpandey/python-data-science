names=["Bruse Wayne","Clark Krent", "Wally West"]  
intials=[]

for name in names:
    parts= name.split()
    intials.append(parts[0][0]+parts[-1][0])  
print(intials)

init=[parts.split()[0][0]+parts.split()[-1][0] for parts in names]
print(init)