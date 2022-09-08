class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Claculation2:
        def multiplication(self,a , b):
            return a*b;
class Derived(Calculation1,Claculation2):
    def Divide(self,a,b):
        return a/b;
    
d= Derived

print(d.Summation(10,20))
print(d.multiplication(10,20))
print(d.Divide(10,20))
        