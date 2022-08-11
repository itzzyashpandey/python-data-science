my_set={1,3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2,3,4])
print(my_set)

my_set.update([4,5],[1,6,8])
print(my_set)

my_set2={1,3,4,5,6}
print(my_set2)

my_set2.discard(4)
print(my_set)

my_set2.remove(6)
print(my_set2)

my_set2.pop()
print(my_set2)

my_set2.clear()
print(my_set2)