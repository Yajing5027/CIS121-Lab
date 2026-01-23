#1
'''
def skip_letter(word):
  #data cleaning
  word = word.replace(' ','')   #string.replace('old', 'new') notice to use parentheses
  letter = []
  for x in word[::2]:   #[]
    letter.append(x)
  return letter

word = input('Enter word: ')
print(skip_letter(word))
'''




#2
'''
def skip_letter(word):
  letter = []
  for x in word[1::2]:
    letter.append(x)
  return letter

word = input('Enter word: ')
print(skip_letter(word))
'''




#3
'''
def output_even(smaller_num,larger_num):
  start = smaller_num + (smaller_num%2)   # guaranteed always even
  return list(range(start,larger_num+1,2))

smaller_num = int(input('Enter smaller number: '))
larger_num = int(input('Enter larger number: '))
print(output_even(smaller_num,larger_num))
'''




#4
'''
def output_odd(smaller_num,larger_num):
  start = smaller_num + (1 - smaller_num%2)   # guaranteed always odd
  return list(range(start,larger_num+1,2))

smaller_num = int(input('Enter smaller number: '))
larger_num = int(input('Enter larger number: '))
print(output_odd(smaller_num,larger_num))
'''




#5
'''
def hailstone_seq(number):
  result = [number]
  while number != 1:
    number = number/2 if number%2==0 else (3*number)+1
    result.append(number)
  return result

number = int(input('Enter number: '))
print(hailstone_seq(number))
'''




#6
'''
def find_factors(num):
  return [x for x in range(1,num+1) if num % x == 0]

num = int(input('Enter number: '))

print(find_factors(num))
'''




#7
'''
def ascending_ording(num_1,num_2,num_3):
  if num_3 > num_2:
    num_2,num_3 = num_3,num_2
  if num_3 > num_1:
    num_1,num_3 = num_3,num_1
  if num_2 > num_1:
    num_1,num_2 = num_2,num_1
  
  return [num_3,num_2,num_1]

num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))
num_3 = int(input('Enter number: '))

print(ascending_ording(num_1,num_2,num_3))
'''




#8
'''
def descending_ording(num_1,num_2,num_3):
  if num_3 > num_2:
    num_2,num_3 = num_3,num_2
  if num_3 > num_1:
    num_1,num_3 = num_3,num_1
  if num_2 > num_1:
    num_1,num_2 = num_2,num_1
  
  return [num_1,num_2,num_3]

num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))
num_3 = int(input('Enter number: '))

print(descending_ording(num_1,num_2,num_3))
'''




#9
'''
def count(cards):
  result = 0
  
  x = [2,3,4,5,6]
  z = [10,'j','q','k','a']

  for n in cards:
    if n in x:
      result += 1
    elif n in z:
      result -= 1
  return result

cards = ['a',5,5,2,6,2,3,8,9,7]
print(count(cards))
'''




#10
'''
def war_of_number(number):
  odd = 0
  even = 0
  for x in number:
    if x%2==1:
      odd += x
    else:
      even += x
  return 'odds' if odd > even else 'evens'

number=[2,8,7,5]
print(war_of_number(number))
'''
#10 simplified version：sum
'''
def war_of_number(number):
  odd = sum(x for x in number if x%2==1)
  even = sum(x for x in number if x%2==0)
  return 'odds' if odd > even else 'evens'

number=[12,90,75,1,1]
print(war_of_number(number))
'''




#11
'''
def add_list(lyst1,lyst2):
  lyst3 = []
  for x in range(0,len(lyst1)):  #the item amount of list
    lyst3.append(lyst1[x] + lyst2[x])
  return lyst3

lyst1 = [1,3,3,1]
lyst2 = [4,3,6,1]
print(add_list(lyst1,lyst2))
'''




#12
'''
def largest_even(number):
  largest = None
  for x in number:
    # None, True, False: use 'is' (except assignment)
    if x % 2 == 0 and (largest is None or x > largest):   # notice: largest is None
      largest = x
  return -1 if largest is None else largest

number = [3,7,2,1,7,9,10,13]

print(largest_even(number))
'''




#13
'''
def largest_odd(number):
  largest = None
  for x in number:
    if x %2 == 1 and (largest is None or x > largest):
      largest = x
  return -1 if largest is None else largest

number = [2,4,6,8]
print(largest_odd(number))
'''




#14
'''
def progress_days(mylist):
  count = 0
  for x in range(1,len(mylist)):
    if mylist[x] > mylist[x-1]:
      count += 1
  return count

mylist = [3,4,1,2]
print(progress_days(mylist))
'''




#15
'''
def lag_days(mylist):
  count = 0
  for x in range(1,len(mylist)):
    if mylist[x] < mylist[x-1]:
      count += 1
  return count

mylist = [5,3,2,1]
print(lag_days(mylist))
'''




#16
'''
def like_or_dislike(button):
  state = None
  for x in button:
    if x != state or state is None:
      state = x
    elif x == state:
      state = 'nothing'
  return state

button = ['like','like']
print(like_or_dislike(button))
'''




#17
'''
def get_indices(mylist,item):
  result = []
  for x in range(0,len(mylist)):
    if str(mylist[x]) == item:    #turn to string
      result.append(x)
  return result

mylist = [1,5,5,2,7]
item = input('Enter item: ')
print(get_indices(mylist,item))
'''




#18
'''
def list_of_multiples(num,length):
  result = []
  for x in range(1,length+1):
    result.append(num * x)
  return result

num = int(input('Enter number: '))
length = int(input('Enter length: '))
print(list_of_multiples(num,length))
'''




#19 Solution path 1:
'''
def is_acronym(words,acronym):
  words_clean = []

  if len(words) != len(acronym):    # avoid ''
    return False

  else:
    for x in range (0,len(words)):
      if acronym[x] != words[x][0]:   #notice: words[x][0]
        return False
  return True

words = ['alice','bob','charlie']
acronym = input('Enter acronym: ')
print(is_acronym(words,acronym))
'''
#19 Solution path 2:
'''
def is_acronym(words,acronym):
  words_acronym = ''

  if len(words) != len(acronym):
    return False
  else:
      for x in words:
        words_acronym += x[0]
  return False if acronym != words_acronym else True

words = ['alice','bob','charlie']
acronym = input('Enter acronym: ')
print(is_acronym(words,acronym))
'''