num=[2,5,4,6,3,45,1,214,7842,3,232,552,3166,569,523,1]
num2=[i%2==0 for i in num]
num3=[i for i in num if i%2==0]
print(num2)
print(num3)