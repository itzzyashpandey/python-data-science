class Shape:
    
    def __init__(self,side):
        self.side=side
        
    def info(self):
        return f'shape with {self.side}'
    
class Rectangle(Shape):
    
    def __init__(self,l,w):
        super().__init__(1)
        self.w=w
        
    def area(self):
        return self.side * self.w 
    
    #over ridden funtion
    def info(self):
        return f'rectangle with 1= {self.side}& w = {self.w}'
    
ob1= Shape(4)
print(ob1.info())

ob2=Rectangle(4,5)
print(ob2.area())
print(ob2.info())        
    
