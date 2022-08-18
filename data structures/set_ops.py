#union
a={1,2,3,4,5,6,6}
b={1,3,8,7,5,3}
c={9}
print(a|b)

print(a.union(b))
print(b.union(a))

#intersection
print(a&b)
print(a.intersection(b))
print(a.intersection(c))

#set difference
print(a-b)
print(b-a)
print(a.difference(b))

#set symmetric difference(uncommon) 

print(a^b)
print(a.symmetric_difference(b))

#check sub set
x={2,3,4,7}
y={2,3,4,7,6,5,8}
print(x.issubset(y))
print(y.issuperset(x))
z={3,5,8,10,11}
print(x.issubset(z))
a={11,12,13}
print(a.isdisjoint(y))
#example
x=[2,2,3,5,5,6,6]
xs=set(x)
xl=list(set(x))

print(x)
print(xs)
print(xl)