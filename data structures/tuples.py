my_tuple=(1,"hello",3.4)
print(my_tuple)

#nested tuple
my_tuple=("mouse", [8,4,6], (1,2,3))
print(my_tuple)

#a tuple can also be createad without using bracket
# this is known as tuple packing
my_tuple=3,4.6,"apple"
print(my_tuple)

#Accessing tuple element using indexing
my_tuple=('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])

#nested tuple accessing 
my_tuple=("mouse", [8,4,6], (1,2,3))
print(my_tuple[0][3])
print(my_tuple[1][1])
print(my_tuple[2][1])


my_tuple=('e','x','c','a','l','i','b','u','r')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

