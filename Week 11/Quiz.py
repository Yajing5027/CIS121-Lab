#1
'''
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def get_major(self):
        return self.major

    def set_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f"Student name: {self.name}, major: {self.major}"


class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students_list = []

    def get_number(self):
        return self.course_number

    def set_number(self, new_number):
        self.course_number = new_number

    def add_student(self, student):
        self.students_list.append(student)

    def show_students_enrollment(self):
        for student in self.students_list:
            print(student)

    def __str__(self):
        return (f"Course: {self.course_name} ({self.course_number})")

student1 = Student("AA","CS")
student2 = Student("BB","Math")

course1 = Course('Math','121')
course1.add_student(student1)
course1.add_student(student2)
print(course1)    
'''




#2
'''
class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def speak(self):
        print("Quack")

    def __str__(self):
        return f"{self.name} the {self.color} duck says Quack"


class Pond:
    def __init__(self, name='unknown'):
        self.name = name
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        for duck in self.ducks:
            duck.speak()

    def __str__(self):
        return f"Pond '{self.name}' has {len(self.ducks)} duck(s)."


duck1 = Duck("Daffy", "black")
duck2 = Duck("Donald", "white")

pond1 = Pond("Sunny Lake")
pond1.add_duck(duck1)
pond1.add_duck(duck2)

pond1.ducks_quack()

print(pond1)
'''




#3
'''
class Lion:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_gender(self):       # add get_gender method for class zoo
        return self.gender

    def roar(self):
        print('Roar')       # print
    
    def __str__(self):
        return f"Lion: {self.name} ({self.gender})"

class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []
    
    def add_lion(self,lion):
        self.lions.append(lion)

    def lion_roar(self):
        for lion in self.lions:
            lion.roar()         # we have set method to print before
    
    def count_lions(self):
        male = 0
        female = 0
        for lion in self.lions:
            if lion.get_gender() == 'male':
                male += 1
            else:
                female +=1
        return f'{male} male, {female} female.'

    def __str__(self):
        return f"Zoo at {self.location} with {len(self.lions)} lions."

lion1 = Lion("Simba", "male")
lion2 = Lion("Nala", "female")

zoo = Zoo("Serengeti")
zoo.add_lion(lion1)
zoo.add_lion(lion2)

zoo.lion_roar()
print(zoo.count_lions())
print(zoo)
'''



#4
'''
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def __str__(self):
        return f"Employee name is {self.name}, and position is {self.position}"


class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget

    def set_budget(self, new_budget):
        self.budget = new_budget

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_staff_list(self):
        for employee in self.employees:
            print(employee)      # print

    def is_large(self):
        return len(self.employees) >= 10        # simplify

    def __str__(self):
        return f"Department {self.dept_name} with budget ${self.budget} has {len(self.employees)} employees."
        

emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")

dept = Department("Engineering", 500000)
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_staff_list()
print(dept)
print("Is large department?", dept.is_large())
'''
    

#5
'''
class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series

    def get_series(self):
        return self.series

    def set_series(self, new_series):
        self.series = new_series

    def communicate(self):
        print("Beep-Bloop-Blop.")       #print

    def __str__(self):
        return f"Droid named {self.designation}, in {self.series} series."


class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []

    def add_droid(self, droid):
        self.droids.append(droid)

    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()     # we have set method to print before

    def __str__(self):
        return f"Starship {self.name} has {len(self.droids)} droids."


droid1 = Droid("AA", "Astromech")
droid2 = Droid("PP", "Protocol")

starship = Starship("Millennium Falcon")
starship.add_droid(droid1)
starship.add_droid(droid2)

starship.droids_communicate()
print(starship)
'''
          
    

#6
'''
class Post:
    def __init__(self, caption, likes=0):
        self.caption = caption
        self.likes = likes

    def get_likes(self):
        return self.likes

    def add_like(self):
        self.likes += 1

    def display(self):
        print(self.caption)     # print

    def __str__(self):
        return f"Post: '{self.caption}' with {self.likes} likes"


class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_trending_posts(self):
        for post in self.posts:
            if post.get_likes() >= 10000:       # judge
                post.display()      # we have set method to print before

    def __str__(self):
        return f"{self.username}'s profile has {len(self.posts)} posts."

post1 = Post("Enjoying the sunset!", 500)
post2 = Post("My new song is out now!", 12000)

profile = Profile("musiclover99")

profile.add_post(post1)
profile.add_post(post2)

print("Trending posts:")
profile.display_trending_posts()

print(profile)
'''




#7
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def display_details(self):
        print(f"The product name is {self.name}, price is ${self.price}.")

    def __str__(self):
        return f"Product name: {self.name}, price: ${self.price}"


class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def __str__(self):
        return f"Shopping cart for customer {self.customer_id} has total price ${self.calculate_total()}."

p1 = Product("Laptop", 1200)
p2 = Product("Headphones", 150)

p1.display_details()
p2.display_details()

cart = ShoppingCart("CUST001")

cart.add_product(p1)
cart.add_product(p2)

print("Total price:", cart.calculate_total())

print(cart)
'''



#8
'''
class LLM:
    def __init__(self, name, token_limit):
        self.name = name
        self.token_limit = token_limit

    def get_token_limit(self):
        return self.token_limit

    def set_token_limit(self, new_limit):
        self.token_limit = new_limit

    def __str__(self):
        return f"LLM name is {self.name}, and token limit is {self.token_limit}."


class AICompany:
    def __init__(self, company_name, founding_year, headquarters):
        self.company_name = company_name
        self.founding_year = founding_year
        self.headquarters = headquarters
        self.llms = []

    def get_headquarters(self):
        return self.headquarters

    def set_headquarters(self, new_headquarters):
        self.headquarters = new_headquarters

    def add_llm(self, llm):
        self.llms.append(llm)

    def display_models(self):
        for llm in self.llms:
            print(llm)      # print

    def __str__(self):
        return (f"AI company name is {self.company_name}, founded in {self.founding_year}")


gpt = LLM("ChatGPT", 128000)
claude = LLM("Claude", 200000)

openai = AICompany("OpenAI", 2015, "San Francisco")

openai.add_llm(gpt)
openai.add_llm(claude)

print("Models developed by the company:")
openai.display_models()

print("Original headquarters:", openai.get_headquarters())
openai.set_headquarters("Austin, Texas")
print("New headquarters:", openai.get_headquarters())

print("Company info:")
print(openai)
'''




#9
'''
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def show_description(self):
        print(f"Menu item name is {self.name}, and price is ${self.price}.")

    def __str__(self):
        return f"Menu item: {self.name}, price: ${self.price}"


class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        for item in self.menu_items:
            print(f'Menu:{item}')

    def lunch_menu(self):
        for item in self.menu_items:
            new_price = item.get_price() - 2            # change price by ues get_price()
            print(f"Lunch Menu: {item.name} — ${new_price}")

    def __str__(self):
        return f"Restaurant '{self.restaurant_name}' has {len(self.menu_items)} menu item(s)."

        
item1 = MenuItem("Cheeseburger", 10)
item2 = MenuItem("Pasta", 12)

restaurant = Restaurant("Gourmet Diner")

restaurant.add_menu_item(item1)
restaurant.add_menu_item(item2)

restaurant.display_menu()

restaurant.lunch_menu()

print(restaurant)
'''




#10
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def display_info(self):
        print(f"{self.title} by {self.author}")

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_catalog(self):
        for book in self.books:
            print(book)

    def __str__(self):
        return f"Library '{self.name}' has {len(self.books)} book(s)."

book1 = Book("Pride and Prejudice", "Jane Austen")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library("City Central Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_catalog()

print(library)
'''

        


#11
'''
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_artist(self, new_artist):
        self.artist = new_artist

    def play(self):
        print(f"{self.title} by {self.artist}")

    def __str__(self):
        return f"'{self.title}' by {self.artist}"


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        return f"Playlist '{self.playlist_name}' has {len(self.songs)} song(s)."

s1 = Song("Shape of You", "Ed Sheeran")
s2 = Song("Bad Guy", "Billie Eilish")
s3 = Song("Believer", "Imagine Dragons")

p = Playlist("My Favorites")

p.add_song(s1)
p.add_song(s2)
p.add_song(s3)

p.play_all()

print(p)
'''        


#12
'''
class TVShow:
    def __init__(self, title="unknown", genre="unknown"):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_genre(self, new_genre):
        self.genre = new_genre

    def preview(self):
        return f"Title: {self.title}, Genre: {self.genre}"

    def __str__(self):
        return f"'{self.title}' ({self.genre})"


class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.dashboard = []

    def add_show(self, show):
        self.dashboard.append(show)

    def display_recommendations(self):
        for show in self.dashboard:
            print(show.preview())

    def __str__(self):
        return f"Netflix Dashboard ({self.profile_name}) has {len(self.dashboard)} show(s)."


show1 = TVShow("Stranger Things", "Sci-Fi")
show2 = TVShow("The Office", "Comedy")
show3 = TVShow("Breaking Bad", "Drama")

dashboard1 = NetflixDashboard("Alice")

dashboard1.add_show(show1)
dashboard1.add_show(show2)
dashboard1.add_show(show3)

dashboard1.display_recommendations()

print(dashboard1)
'''    

