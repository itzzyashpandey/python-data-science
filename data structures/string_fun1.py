name="yash pandey MY name"

print(name.upper())
print(name.capitalize())
print(name.lower())
print(name.title())
print(name.swapcase())
print(name.casefold())


val=5



words="python"
#left align

print(words.ljust(80))



print(words.rjust(80))



print(words.center(80))



print(words.ljust(80,'-'))



print(words.rjust(80,'$'))



print(words.center(80,'@'))
#____________________________________________________________________________________#






print('-'*40)
for i in range(1,21):
    r=3**i
    print(3,'pow',str(i).rjust(2),'=',r)