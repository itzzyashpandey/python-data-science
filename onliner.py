#val=int(input("enter a number"))
#if val >100:
#    val = val/2
#else:
#    val=val*2
#print("the result is", val)

#to print in online

val=int(input("enter a number"))
val=val/2 if val>100 else val * 2
print("the result is", val)

name= input("enter ur name")
print("very good") if name.isalpha() else print("not good")