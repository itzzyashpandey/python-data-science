class Movie:
    def __init__(self,title,rating,year):
        self.title=title
        self.rating=rating
        self.year=year
        
    def info(self):
        print( f'''movie title {title}
    movie rating {rating} in {year}''')
        
    def __gt__(self,other):
        if self.rating> other.rating:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.rating< other.rating:
            return True
        else:
            return False
        
    def __repr__(self):
        return self.title
    
m=Movie('no entry', 4.0, 2007)  
m2= Movie('liger', 1,2022)  

print(m>m2)
print(m2>m) 

movies=[m,m2]
movies.sort()
print(movies)
       
    
        

    
    
        