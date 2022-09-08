
#loops
x=[2,5,10,7]
x2=[]
for i in x:
    s=i**2
    x2.append(s)
print(x2)    

x=[2,3,5,4]
y=[3,6,5,3]
z=[]

for i,j in zip(x,y):
    s=i+j
    z.append(s)
print(z)

names=["Bruse Wayne","Clark Krent", "Wally West"]  
intials=[]

for name in names:
    parts= name.split()
    intials.append(parts[0][0]+parts[-1][0])  
print(intials)
#comprehension
x=[2,5,4,6,7,8,4,9]
x2=[i**2 for i in x]
print(x2)


x=[2,3,5,4]
y=[3,6,5,3]
z=[i+j for i,j in zip(x,y)]
print(z)



#there are three method to solve these type of question
#existing list to new list  
#1: loops
#2:comprehension
#3: Lambda expresion