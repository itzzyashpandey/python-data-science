from turtle import *

side=6
size=50
pensize(5)
for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(6):
        pencolor('blue')
        
        forward(25)
        left(360/6)
        write(i, font=('arial', 14, 'normal'))
    left(360/side)

mainloop()    