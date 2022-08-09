x="python"
for i in x:
    print(i)
    
fruits= ["apple", "banana", "lemon"]
for item in fruits:
    print(f'i have {item}')    
    

for j in range(0,101,1): #only middle filed is compulsory
    print(j)
    
for j in range(5,101,2):
    print(j)    
    
    
x=[2,3,5,4]
y=[3,6,5,3]
z=[]

for i,j in zip(x,y):
    s=i+j
    z.append(s)
print(z)        