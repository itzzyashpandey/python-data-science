import pgzrun

WIDTH = 700
HEIGHT = 500

#actor
p = Actor('char1',(50,200))

def draw():
    screen.fill('white')
    p.draw()
    
def update():