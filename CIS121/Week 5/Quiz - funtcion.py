#1
'''
def pyramid_volume (b,h):
  return round(((b**2)*h)/3 , 2)    #round(expression, 2) -> Round to two decimal places

print(pyramid_volume(1,2))
'''




#2
'''
import math
def cone_volume(r,h):
  return round((math.pi)*(((r**2)*h)/3),2)

print(cone_volume(1,2))
'''




#3
'''
def total_score(two,three):
  return((two*2)+(three*3))
print(total_score(5,7))
'''




#4
'''
def total_score(ace,win):
  return((ace*2)+(win*1))
print(total_score(2,3))
'''




#5
'''
def leg_counter(chickens,cows,pigs):
  return((chickens*2)+(cows*4)+(pigs*4))
print(leg_counter(4,3,2))
'''




#6
'''
def battery_counter(dolls,cars,dogs):
  return((dolls*2)+(cars*4)+(dogs*6))
print(battery_counter(4,3,2))
'''




#7
'''
def resting_rate(age,goal):
  above = {(20,39+1):'47-72',(40,59+1):'46-71',(60,79+1):'45-70'}
  below = {(20,39+1):'73-93',(40,59+1):'72-94',(60,79+1):'71-97'}
  return above.get(age,'Unknown') if goal == 'Above Average' else below.get(age,'Unknown')

age = int(input('Enter age: '))
goal = input('Enter athletic goal: ')

print(resting_rate(age,goal))
'''




#8
'''
def pool_time (grade,time):
  result=''

  if grade =='K':
    grade == 0

# variable = expression -> 「value_if_true if condition else value_if_false」
# result = 「'9AM' if time == 'Morning' else '1PM'」
# Notice!!! result = '10AM' if time == 'Morning' else 「result =」 '2PM' is wrong!!
  if 0 <= grade <=3:
      result = '9AM' if time == 'Morning' else '1PM'
  elif 4 <= grade <= 8:
      result = '10AM' if time == 'Morning' else '2PM'
  elif 9 <= grade <= 12:
      result = '11AM' if time == 'Morning' else '3PM'

  return result


garde = input('Enter the grade: ')
time = input('Enter the time: ')

print(f'The pool time is {pool_time(grade,time)}')
'''




#9
'''
def light_color(color):
  rules = {'Red':'Stop', 'Green':'Go', 'Yellow':'Yield'}
  return rules[color]


color = input('Enter color: ')

print(light_color(color))
'''




#10
'''
def access_rights(role):
  rules = {'user':'limited', 'guest':'view', 'admin':'full'}
  return rules[role]


role = input('Enter role: ')

print(access_rights(role))
'''




#11
'''
def convert_kunts (kunts):
  g = ''
  s = ''
  k = ''

  if kunts >= 29:
    sickle = kunts // 29
    s = f'{sickle} sickles' + ' '
    if sickle == 1:
      s = f'{sickle} sickle' + ' '
    kunts %= 29
    if kunts > 0:
      k = f'{kunts} kunts'
    if sickle >= 17:
      galleon = sickle // 17
      g = f'{galleon} galleons' + ' '
      if galleon == 1:
        g = f'{galleon} galleon' + ' '
      sickles = sickle % 17
      if sickles > 0:
        s = f'{sickles} sickles' + ' '
        if sickles == 1:
          s = f'{sickles} sickle' + ' '
      else:
        s = ''
    else:
      k = f'{kunts} kunts'
      if kunts == 1:
        k = f'{kunts} kunt'

  return g + s + k

kunts = int(input('Enter kunts counts: '))

print(convert_kunts(kunts))
'''
#11 simplified verison:
'''
def convert_kunts (kunts):
  galleon = kunts // (29*17)
  kunts %= 29*17

  sickle = kunts // 17
  kunts %= 17

  result = []
  if galleon > 0:
    result.append(f"{galleon} galleon{'s' if galleon>1 else ''}")
  if sickle > 0:
    result.append(f"{sickle} sickle{'s' if sickle>1 else ''}")
  if kunts > 0:
    result.append(f"{kunts} kunt{'s' if kunts>1 else ''}")

  return ' '.join(result)   #"separator".join(list)

kunts = int(input('Enter kunts counts: '))

print(convert_kunts(kunts))
'''




#12
'''
def convert_bronze(bronze):
  gold = bronze // (20*15)
  bronze %= (20*15)

  silver = bronze // 15
  bronze %= 15

  result = []

  if gold>0:
    result.append(f'{gold} gold')
  if silver>0:
    result.append(f'{silver} silver')
  if bronze>0: result.append(f'{bronze} bronze')

  return ' '.join(result)

bronze = int(input('Enter bronze coins: '))

print(convert_bronze(bronze))
'''




#13
'''
from random import randint
value = randint(0,1) #inclusive of both endpoints

def toss_cion(guess):

  return 'Correct!' if guess == value else 'Incorrect!'


guess = int(input('Enter your guess (0 or 1): '))

print(toss_cion(guess))
'''




#14
'''
from random import randint
value = randint(0,9) #inclusive of both endpoints

def guess_num(guess):
  result = 'odd' if value%2 == 1 else 'even'
  return 'Correct!' if guess == result else 'Incorrect!'


guess = input('Enter your guess: ')

print(guess_num(guess))
'''




#15
'''
def count_duplicates (num_1,num_2,num_3):
  if num_1==num_2==num_3:
    count=3
  elif num_1==num_2 or num_2==num_3 or num_1==num_3:
    count=2
  else:
    count=0
  return count

num_1 = float(input('Enter your number: '))
num_2 = float(input('Enter your number: '))
num_3 = float(input('Enter your number: '))

result = count_duplicates (num_1,num_2,num_3)

if result == 0:
  print('Each number is unique.')
else:
  print(f'You entered the same number {result} times.')
'''




#16
'''
def highway_direction(number):
  if number > 99:
    number %= 100
    if number == 0:
      return 'is an invalid highway number'
    return 'runs north/south' if number%2==1 else 'runs east/west'
  else:
    return 'runs north/south' if number%2==1 else 'runs east/west'


number = int(input('Enter number: '))

print(f'I-{number} {highway_direction(number)}')
'''




#17
'''
def check_letter(letter):
  result = ''
  my_list = ['a','e','i','o','u']

# simplified version: remove result
  if letter in my_list:
    return 'Vowel'
  return 'Consonant'

letter = input('Enter letter: ')

print(check_letter(letter))
'''

'''
  if letter in my_list:
    result = 'Vowel'
  else:
    result = 'Consonant'

  return result
'''




#18
'''
def serve_icecream(icecream):
  icecream_list = ['Vanilla', 'Chocolate', 'Strawberry']
  return f'Here is your {icecream} ice cream!' if icecream in icecream_list else f"Sorry, we don't have {icecream} ice cream."

icecream = input('Enter your icecream: ')

print(serve_icecream(icecream))
'''



#19
'''
def serve_coffee(coffee):
  coffee_list = ['espresso','latte','cappuccino']
  return f'Here is your {coffee}!' if coffee in coffee_list else f"Sorry, we don't have {coffee}."

coffee = input('Enter your coffee: ')

print(serve_coffee(coffee))
'''




#20
'''
def find_winner(player_1,player_2):
  if player_1 == player_2:
    return "It's a tie!"
  else:
    if player_1 == 'Rock':
     return 'Player 1 wins!' if player_2 == 'Scissors' else 'Player 2 wins!'
    elif player_1 == 'Scissors':
     return 'Player 1 wins!' if player_2 == 'Paper' else 'Player 2 wins!'
    else:
     return 'Player 1 wins!' if player_2 == 'Rock' else 'Player 2 wins!'

player_1 = input('Enter your choice: ')
player_2 = input('Enter your choice: ')

print(find_winner(player_1,player_2))
'''
#20 simplified version: dictionary
'''
def find_winner(player_1,player_2):

  if player_1 == player_2:
    return "It's a tie!"

  #dictionary = {key_1:value_1, key_2:value_2} notice: key is string -> 'key'.
  rules = {'Rock':'Scissors', 'Scissors':'Paper', 'Paper':'Rock'}
  if rules[player_1]==player_2:   #dicitionary[key] -> get value
    return 'Player 1 wins!'
  else:
    return 'Player 2 wins!'

player_1 = input('Enter your choice: ')
player_2 = input('Enter your choice: ')

print(find_winner(player_1,player_2))
'''




#21
'''
def triangle(side_1,side_2,side_3):
  result = ''
  if side_1 == side_2 == side_3:
    result = 'equilateral'
  elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    result = 'isosceles'
  else:
    result = 'scalene'
  return result

side_1 = float(input('Enter side_1: '))
side_2 = float(input('Enter side_2: '))
side_3 = float(input('Enter side_3: '))

print(triangle(side_1,side_2,side_3))
'''




#22
'''
def find_relation(name):
  relations = {'Darth Vader':'Father','Leia':'Sister','Han':'Brother in law','R2D2':'Droid'}
  # dict.get(key, default=None)
  return relations.get(name, 'Unknown')

name = input('Enter name: ')

print(find_relation(name))
'''




#23
'''
def find_relation(role):
  relations = {'Moriarty':'Archenemy','Watson':'Best Friend','Mrs.Hudson':'Landlady','Inspector Lestrade':'Detective'}
  return relations.get(role, 'Unknow')

role = input('Enter role: ')

print(find_relation(role))
'''




#24
'''
def skip_letter(word):
  return word[1::2]

word = input('Enter word: ')

print(skip_letter(word))
'''




#25
'''
def skip_letter(word):
  #data cleaning
  word = word.replace(' ','')   #string.replace('old', 'new') notice to use parentheses
  return word[::2]
word = input('Enter word: ')

print(skip_letter(word))
'''




#26
'''
def output_even(smaller_num,larger_num):
  if smaller_num %2 == 1:
    smaller_num += 1
  mylist = []
  for x in range(smaller_num,larger_num+1,2):
    mylist.append(x)
  return mylist


smaller_num = int(input('Enter smaller_num: '))
larger_num = int(input('Enter larger_num: '))

print(output_even(smaller_num,larger_num))
'''
#26 simplified version: guaranteed always even + list(iterable) / list comprehension
'''
def output_even(smaller_num,larger_num):
  start = smaller_num + (smaller_num %2)    # guaranteed always even
'''
'''
  list() Function: list(iterable)

  list(range(5))           # [0, 1, 2, 3, 4]
  list("abc")              # ['a', 'b', 'c']
  list((1, 2, 3))          # [1, 2, 3]
'''
'''
  return list(range(start,larger_num+1,2))

  #list comprehension: [expression for item in iterable if condition]
  return [x for x in range(start,larger_num+1,2)]


smaller_num = int(input('Enter smaller_num: '))
larger_num = int(input('Enter larger_num: '))

print(output_even(smaller_num,larger_num))
'''




#27
'''
def odd_sum(smaller_num,larger_num):
  start = smaller_num + (1 - smaller_num%2)   # guaranteed always odd
  total = 0
  for x in list(range(start,larger_num+1,2)):
    total += x
  return total

smaller_num = int(input('Enter smaller_num: '))
larger_num = int(input('Enter larger_num: '))

print(odd_sum(smaller_num,larger_num))
'''




#28
'''
def create_word():    #no arguments
  letter_list = []
  letter = input('Enter a letter (or type done): ')
  while letter != 'done':
    letter_list.append(letter)
    letter = input('Enter a letter (or type done): ')
  return ''.join(letter_list)

print(create_word())
'''




#29
'''
def sum_loop():
  total = 0
  num = int(input('Enter an integer: '))
  while num >= 0:
    total += num
    num = int(input('Enter an integer: '))
  return total

print(sum_loop())
'''




#30
'''
def hailstone_seq(n):
  result = [n]
  while n!=1:
    n = n/2 if n%2==0 else (n*3)+1
    result.append(n)
  return result

n = int(input('Enter a positive integer: '))

print(hailstone_seq(n))
'''




#31
'''
def find_factors(num):
  return [x for x in range(1,num+1) if num % x == 0]

num = int(input('Enter number: '))

print(find_factors(num))
'''




#32
'''
def design_run(width,length,pattern):
  collection = []
  for x in range(1,length+1):
    collection.append(pattern * width)
  return '\n'.join(collection)    #'\n' means line break
        #"separator".join(list)


width = int(input('Enter width: '))
length = int(input('Enter length: '))
pattern = input('Enter : ')


print(design_run(width,length,pattern))
'''




#33
'''
def square_sum(num):
  return sum((x**2) for x in range(1,num+1)) if num>0 else 'Unknown'

num = int(input('Enter number: '))

print(square_sum(num))
'''




#34
'''
def cube_sum(num):
  return sum((x**3) for x in range(1,num+1)) if num>0 else 'Unknown'

num = int(input('Enter number: '))

print(cube_sum(num))
'''












