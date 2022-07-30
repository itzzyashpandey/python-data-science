from turtle import *

start = 200
while start > 0:
    forward(start)
    left(360/5)
    start-= 5
    write(start , font=('arial', 14 , 'normal'))
    
mainloop()    