
class Dog:
    breed=""
    age = 0
    color=''
    weight=0
    height=0
    gender=''
    
    def bark(self):
        print('🐶bow'*3)
        
    def wag(self):
        print('wag tails🐕‍🦺')
        
    def eat(self,food):
        print(f'dog {food} kha ragha hai dog')
        
tommy= Dog()
tommy.age=3
tommy.breed='street'
tommy.color='black'
tommy.gender='male'
tommy.height='2'
tommy.weight=5
charlie= Dog()
charlie.age=4
charlie.breed='german spheard'
charlie.color='black-brown'
charlie.gender='female'
charlie.height='3'
charlie.weight=15
jimmy= Dog()
jimmy.age=5
jimmy.breed='labra'
jimmy.color='white'
jimmy.gender='male'
jimmy.height='1'
jimmy.weight=10

jimmy.bark()
jimmy.eat('fish')
charlie.eat('dog-food')
tommy.eat('bachi hui roti')
tommy.bark()
jimmy.bark()

    
