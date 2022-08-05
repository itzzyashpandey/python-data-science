x=[1,1,1,1,1,1,1,1,1,1,13,3,3,2,3,3,3,3,5,5,5,6,5,65,65,6,]

print("total no of 3=",x.count(3))
print("total no of 1=",x.count(1))
print("total no of 2=",x.count(2))
print("total no of 5=",x.count(5))
print("total no of 6=",x.count(6))
print("total no of 99=",x.count(99))

movies=["john wick", "thor","black panther", "KGF", "RRR","krish","dr.strange"]

print(movies.index("dr.strange"))

#print(movies.index("3 ediots"))

blockbusters=movies.copy()
print(blockbusters)

blockbusters.clear()
print(blockbusters)


print("after poping=",movies.pop())
print(movies)

print("after pop at 2=",movies.pop(2))
print(movies)
