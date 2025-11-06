#1
'''
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name

    
    def get_price(self):
        return self.price
    def set_price(self,new_price):
        self.price = new_price
    
    def get_quantity(self):
        return self.quantity
    def set_quantity(self,new_quantity):
        self.quantity = new_quantity
    
    
product1 = Prouduct('apple',3.5,10)
print(product1.get_name())
print(product1.get_price())
print(product1.get_quantity())

product1.set_name('pear')
print(product1.get_name())
'''




#2
'''
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author
    def set_author(self, new_author):
        self.author = new_author

    def get_page_count(self):
        return self.page_count
    def set_page_count(self, new_page_count):
        self.page_count = new_page_count
    
book1 = Book('abcde', 'aa', 193)
print(book1.get_title())
print(book1.get_author())
print(book1.get_page_count())

book1.set_title('12345')
print(book1.get_title())
'''




#3
'''
class Movie:
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title

    def get_director(self):
        return self.director
    def set_director(self, new_director):
        self.director = new_director

    def get_runtime_minutes(self):
        return self.runtime_minutes
    def set_runtime_minutes(self, new_runtime_minutes):
        self.runtime_minutes = new_runtime_minutes


movie1 = Movie('aa', 'bb', 148)
print(movie1.get_title())
print(movie1.get_director())
print(movie1.get_runtime_minutes())

movie1.set_director('vv')
print(movie1.get_director())
'''




#4
'''
class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title
    
    def get_artist(self):
        return self.artist
    def set_artist(self, new_artist):
        self.artist = new_artist

    def get_duration_seconds(self):
        return self.duration_seconds
    def set_duration_seconds(self, new_duration_seconds):
        self.duration_seconds = new_duration_seconds

song1 = Song('aa', 'bb', 354)
print(song1.get_title())
print(song1.get_artist())
print(song1.get_duration_seconds())

song1.set_title('cc')
print(song1.get_title())
'''




#--------------------------------------------------------------------




#5
'''
class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
    
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title

    def get_salary(self):
        return self.salary
    def set_salary(self, new_salary):
        self.salary = new_salary
    
    def greeting(self):
        return f"Hello. My name is {self.name}. I'm the {self.title}."
    
    def request_raise(self):
        new_salary_amount = self.salary * 1.06
        return f"I'm currently making ${self.salary:.f}. I'd like new salary of ${new_salary_amount:.2f}." 

employee1 = Employee('Eugene', 'CEO', 100)
print(employee1.greeting())
print(employee1.get_salary())
employee1.set_title('Senior CEO')
print(employee1.get_title())
print(employee1.request_raise())
'''




#6
'''
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    
    def get_major(self):
        return self.major
    def set_major(self, new_major):
        self.major = new_major

    def get_gpa(self):
        return self.gpa
    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:       # condition
            self.gpa = new_gpa
    
    def introduce(self):
        return f"Hi, I'm {self.name}. I'm studying {self.major}."

    def study_for_exam(self):
        old_gpa = self.gpa
        new_gpa = self.gpa + 0.2
        self.gpa = new_gpa
        if self.gpa >= 4.0: 
            self.gpa = 4.0            
        # control the number of decimal places “:.1f” 1 decimal place
        return f"I'm hitting the books! My GPA increased from {old_gpa:.1f} to {self.gpa:.1f}."


student1 = Student('Maria', 'Computer Science', 3.5)
print(student1.study_for_exam())
print(student1.get_gpa())
'''




#7
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    def set_make(self, new_make):
        self.make = new_make

    def get_model(self):
        return self.model
    def set_model(self, new_model):
        self.model = new_model

    def get_year(self):
        return self.year    
    def set_year(self, new_year):
        self.year = new_year
    
    def print_vehicle_type(self):
        return f"{self.year} {self.make} {self.model}"


vehicle1 = Vehicle('Toyota', 'Camry', 2021)

print(vehicle1.print_vehicle_type())
print(vehicle1.get_make())

vehicle1.set_year(2022)
print(vehicle1.get_year())
'''




#8
'''
class Course:
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
    
    def get_course_code(self):
        return self.course_code
    def set_course_code(self, new_course_code):
        self.course_code = new_course_code

    def get_course_name(self):
        return self.course_name
    def set_course_name(self, new_course_name):
        self.course_name = new_course_name

    def get_instructor(self):
        return self.instructor
    def set_instructor(self, new_instructor):
        self.instructor = new_instructor
    
    def print_info(self):
        return f"{self.course_code}: {self.course_name} taught by {self.instructor}"


course1 = Course('CIS101', 'Introduction to programming', 'Matt')

print(course1.print_info())
print(course1.get_course_code())

course1.set_instructor('Dr. Smith')
print(course1.get_instructor())
'''




#9
'''
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.x_coordinate
    def set_x_coordinate(self, new_x):
        self.x_coordinate = new_x

    def get_y_coordinate(self):
        return self.y_coordinate
    def set_y_coordinate(self, new_y):
        self.y_coordinate = new_y

    def print_info(self):        
        return f'(x,y)=({self.x_coordinate},{self.y_coordinate})'


point1 = Point(4, 5)
print(point1.print_info())

point1.set_x_coordinate(10)
point1.set_y_coordinate(20)
print(point1.print_info())

print(point1.get_x_coordinate())  
print(point1.get_y_coordinate())  
'''




#10
'''
class Vector:
    def __init__(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction

    def get_x_direction(self):
        return self.x_direction
    def set_x_direction(self, new_x):
        self.x_direction = new_x

    def get_y_direction(self):
        return self.y_direction
    def set_y_direction(self, new_y):
        self.y_direction = new_y

    def get_magnitude(self):
        return (self.x_direction**2 + self.y_direction**2) ** 0.5


vector1 = Vector(3, 4)
print(vector1.get_magnitude())  

vector1.set_x_direction(6)
vector1.set_y_direction(8)
print(vector1.get_magnitude())  
'''        




#11
'''
class ColorRGB:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def get_red(self):
        return self.red
    def set_red(self, new_red):
        self.red = new_red

    def get_green(self):
        return self.green
    def set_green(self, new_green):
        self.green = new_green

    def get_blue(self):
        return self.blue
    def set_blue(self, new_blue):
        self.blue = new_blue

    def to_grayscale(self):
        return 0.3 * self.red + 0.59 * self.green + 0.11 * self.blue


color1 = ColorRGB(255, 0, 0)  
print(f"Grayscale of color1: {color1.to_grayscale()}") 

color1.set_green(255)
color1.set_blue(255)
print(f"Grayscale of updated color1: {color1.to_grayscale()}")

print(f"Red component: {color1.get_red()}")
print(f"Green component: {color1.get_green()}")
print(f"Blue component: {color1.get_blue()}")
'''




#12
'''
class TemperatureInCelsius:
    def __init__(self, temp_value=0):
        self.temp_value = temp_value

    def get_temp_value(self):
        return self.temp_value
    def set_temp_value(self, new_temp_value):
        self.temp_value = new_temp_value

    def to_fahrenheit(self):
        return (self.temp_value * 9 / 5) + 32



temp1 = TemperatureInCelsius(25)
print(f"Temperature in Fahrenheit: {temp1.to_fahrenheit()}")  

temp1.set_temp_value(0)  
print(f"Temperature in Fahrenheit: {temp1.to_fahrenheit()}")  
print(f"Current Celsius temperature: {temp1.get_temp_value()}")
'''




#13
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    def set_width(self,new_width):
        self.width = new_width

    def get_height(self):
        return self.height
    def set_height(self,new_height):
        self.height = new_height

    def calculate_area(self):
        return self.width * self.height


rectangle1 = Rectangle(10, 5)

print(rectangle1.calculate_area())
print(rectangle1.get_width())

rectangle1.set_height(7)
print(rectangle1.get_height()) 
'''




#14
'''
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius


    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.radius = new_radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(5)
print(circle1.calculate_circumference())
'''




#15
'''
class Recipe:
    def __init__(self, name, cooking_time=0):
        self.name = name
        self.cooking_time = cooking_time

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, new_cooking_time):
        self.cooking_time = new_cooking_time

    def is_quick_meal(self):
        return self.cooking_time < 30


recipe1 = Recipe("Pasta", 25)
print(recipe1.is_quick_meal())

recipe1.set_cooking_time(45)
print(recipe1.is_quick_meal())  

print(recipe1.get_name()) 
print(recipe1.get_cooking_time()) 
'''