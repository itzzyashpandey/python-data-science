from tokenize import maybe


my_dict={'name': "jack", "age":26, }

print(my_dict['name'])
print(my_dict.get("age"))
#print(my_dict["adress"])
print(my_dict.get("address"))

my_dict["age"]=27
print(my_dict)

my_dict["address"]="downtown"
print(my_dict)


#to remove a element
my_dict.popitem()
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.clear()
print(my_dict)