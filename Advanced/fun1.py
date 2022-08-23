#sntax
#def fun_name([parameter]):
#  statements
#  [ retun expersion ]

def hello():
    print('👋 hello')
    print('world 🌏')

#calling  or using
hello()
hello()

def greetings(msg):
    print(msg)
    
greetings('world')
greetings("hola amigos")
greetings("sasri kaal")
greetings("namste")


def cal_area(w,h):
    area= w*h
    print('area:', area)

cal_area(10,30)
cal_area(20,30)
cal_area(40,30)


#return value wale 

def calc_area_v2(w,h):
    area = w*h
    return area

print(calc_area_v2(10,2))
print(calc_area_v2(3,5))

#storing return value in a variable 
ans= calc_area_v2(5,5)
print(ans)

#using return values in a expresion 
ans=calc_area_v2(3,5)+ calc_area_v2(3,5)
print(ans)