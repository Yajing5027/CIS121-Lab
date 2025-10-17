# 1
'''
def toss_coin(guess = 0):
  from random import randint
  value = randint(0,1)
  return "Correct!" if value == guess else "Incorrect!"

guess = input('Enter your guess: ')
print(toss_coin())
'''




# 2
'''
from random import randint

def guess_oe(guess = 'even'):
  value = randint(0,9)
  value = 'odd' if value %2 ==1 else 'even'
  return "Correct!" if value == guess else "Incorrect!"

guess = input('Enter your : ')
print(guess_oe())
'''




# 3
'''
def count_duplicates(num_1=0,num_2=0,num_3=0):

  if num_1 == num_2 == num_3:
    return "There are 3 of the same number"
  elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    return "There are 2 of the same number"
  else:
    return "Each number is unique"

print(count_duplicates(0))
'''




# 4
'''
def find_winner(player1 = 'Rock',player2 = 'Rock'):
  role = {'Rock':'Scissors','Paper':'Rock','Scissors':'Paper'}

  if player1 == player2:
    return "It's a tie!"
  else:
    return "Player 1 wins!" if role[player1] == player2 else 'Player 2 wins!'

print(find_winner(player2 = 'Paper'))
'''





# 5
'''
def find_relation(name=''):
  relations = {'Darth Vader':'Father','Leia':'Sister','Han':'Brother in law','R2D2':'Droid'}
  # dict.get(key, default=None)
  return relations.get(name, 'Unknown')

name = input('Enter name: ')

print(find_relation(name)) if name else print(find_relation())
'''




# 6
'''
def hailstone_seq(n=40):
  n = int(n)
  result = [n]

  while n != 1:
      n = n/2 if n%2==0 else 3*n+1
      result.append(n)
  return result

n = input('Enter your number: ')
print(hailstone_seq())
'''




# 7
'''
def ascending_order(num_1,num_2=5,num_3=25):
  if num_1 < num_2:
    num_1,num_2 = num_2,num_1
  if num_1 < num_3:
    num_1,num_3 = num_3,num_1
  if num_2 < num_3:
    num_2,num_3 = num_3,num_2
  return [num_1,num_2,num_3]

print(ascending_order(50))
'''




# 8
'''
def ascending_order(num_1,num_2=15,num_3=5):
  if not num_2:
    num_2 = 5
  if not num_3:
    num_3 = 25

  if num_1 > num_2:
    num_1,num_2 = num_2,num_1
  if num_1 > num_3:
    num_1,num_3 = num_3,num_1
  if num_2 > num_3:
    num_2,num_3 = num_3,num_2
  return [num_1,num_2,num_3]

num_1 = int(input('Enter your number: '))
num_2 = int(input('Enter your number: '))
num_3 = int(input('Enter your number: '))
print(ascending_order(num_1,num_2,num_3))
'''




# 9
'''
def get_indices(mylist,value = 0):
  squence = []
  for x in range(0,len(mylist)):
    if value == mylist[x]:
      squence.append(x)
  return squence

mylist = [1,0,5,0,7]
value = input('Enter your value: ')
print(get_indices(mylist))
'''




# 10
'''
def find_factor(num=36):
  result = []
  for x in range(1,num+1):
    if num % x == 0:
      result.append(x)
  return result

print(find_factor(12))
'''




# 11
'''
def list_of_multiples(num,length = 5):
  result = []
  for x in range(1,length+1):
    result.append(num*x)
  return result

print(list_of_multiples(2))
'''




# 12
'''
def is_even(x):
  return x%2==0

def report_evens(numlist):
  result = []
  for x in numlist:
    if is_even(x):
      result.append(x)
  return result
  
numlist = [4,3,12,16,8,9,25]

print(report_evens(numlist))
'''




# 13
'''
def is_vowel(x):
  return True if x in ['a','e','i','o','u'] else False

def report_evens(word):
  result = []
  for x in word:
    if is_vowel(x):
      result.append(x)
  return result

word = input('Enter your word: ')
print(report_evens(word))
'''




# 14
'''
def is_two_digit_numbers(x):
  return True if x in range(-99,-10+1) or x in range(10,99+1) else False
  # notice end+1

def report_two_digit_numbers(numlist):
  result = []
  for x in numlist:
    if is_two_digit_numbers(x):
      result.append(x)
  return result


numlist = [100,57,12,1,-10]
print(report_two_digit_numbers(numlist))
'''



# 15
'''
def is_negative(x):
  return True if x < 0 else False

def is_odd(x):
  return True if x%2 == 1 else False

def report_negative_odds(mylist):
  result = []
  for x in mylist:
    if is_negative(x) and is_odd(x):
      result.append(x)
  return result

mylist = [100,-57,12,1,-36,-15]
print(report_negative_odds(mylist))
'''