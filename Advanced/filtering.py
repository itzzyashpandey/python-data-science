a=[1,2,2,1,3,1,3,2,13,2,3,3,2,1,2,3,2,1,1,2,3,1,3]

clean_a=list(filter(lambda i: i!=1, a))
print(clean_a)

files=['a.png','b.jpg','c.jpg','d.png']
jpeg=list(filter(lambda name: name.endswith('.jpg'),files))
png=list(filter(lambda name: name.endswith('.png'),files))
print(jpeg)
print(png)