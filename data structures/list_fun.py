from importlib.util import source_hash


fruits=[]

fruits.append("mango")
fruits.append("apple")
fruits.append("banana")
fruits.append("kiwi")

print(fruits)

if 'Mango' in fruits:
    print(1)
else:
    print(0)

fruits.insert(2,"strawberry")
print(fruits)

dry_fruits=["almonde","cashew","walnut", "dates", "rasins"]

merge_list=[]

fruits.extend(dry_fruits)
print(fruits)
#merge_list=fruits
#print(merge_list)
fruits.sort()

print(fruits)

fruits.remove("dates")
print(fruits)
#fruits.remove("berybery")
#print(fruits)

fruits.sort(reverse=True)
print(fruits)
