#1
'''
class Vetor:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        return self.a == value.a and self.b == value.b      # judge don't need to renew class 
    
    def __str__(self):
        a = self.a
        b = self.b
        if a == 0:
            return f'{b} y'
        elif b == 0:
            return f'{a} x'
        else:
            return f'{a} x + {b} y' if b>0 else f'{a} x - {abs(b)} y'       # abs() - absolute value
'''




#2
'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def distance(self,other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance
    
    def __str__(self):
        return f'({self.x},{self.y})'
'''




#3
'''
class LinearEquation:
    def __init__(self,m,b):
        self.m = m
        self.b = b

    def __add__(self,other):
        m = self.m + other.m
        b = self.b + other.b
        return LinearEquation(m,b)      # renew class

    def __str__(self):
        return f'y = {self.m}x + {self.b}'
'''




#4
'''
class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __add__(self,other):
        extra_hours = (self.minutes + other.minutes) // 60
        if  extra_hours >= 1:
            hours = self.hours + other.hours + extra_hours
            minutes = (self.minutes + other.minutes) % 60
            return Time(hours,minutes)
        else:
            hours = self.hours + other.hours
            minutes = self.minutes + other.minutes
            return Time(hours,minutes)
    
    def __str__(self):
        return f'{self.hours} hours {self.minutes} mintues'
'''





#5
'''
class RGBColor:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self,other):
        r = (self.r + other.r)/2
        g = (self.g + other.g)/2
        b = (self.b + other.b)/2

        if r > 225:
            r = 225
        if g > 225:
            g = 225
        if b > 225:
            b = 225

        return RGBColor(r,g,b)
    
    def __str__(self):
        return f'RGB({self.r},{self.g},{self.b})'
'''        


        


#6
'''
class RationalNumber:
    def __init__(self,numerator,denominator):
        self.n = numerator
        self.d = denominator
    
    def __add__(self,other):
        if self.d == other.d:
            n = self.n + other.n
            return RationalNumber(n,self.d)
        
        else:
            d = self.d * other.d
            n = self.n * other.d + other.n * self.d
            return RationalNumber(n,d)

    def __str__(self):
        return f'{self.n}/{self.d}'
'''    

        


#7

class ComplexNumber:
    def __init__(self,real_part,imaginary_part):
        self.r = real_part
        self.i = imaginary_part
    
    def __eq__(self, value):
        return self.r == value.r and self.i == value.i
    
    def __str__(self):
        if self.i == 0:
            return f'z = {self.r}'
        else:
            return f'z = {self.r} + {self.i}' if self.i > 0 else f'z = {self.r} - {abs(self.i)}'        # abs
        


#8

class PLaylist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    
    def add_song(self,song):
        self.songs.append(song)
    
    def __add__(self,other):
        for song in other.songs:
            self.songs.append(song)
    def __str__(self):
        return ','.join(self.songs)     # dont's use list comprehension
    
#9

class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self,other):
        for item in other.items:
            if item in self.items:
                self.items[item] += other.items[item]
            else:
                self.items[item] = other.items[item]

    def __str__(self):
        return '\n'.join(self.items)
        




#10

class Recarangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width*self.height
    
    def __mul__(self,n):
        w = self.width*n
        h = self.height*n
        return ()
    
    def __str__(self):
        return f'Rectangle({self.width} x {self.height})'