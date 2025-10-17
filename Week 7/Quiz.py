#1
'''
def is_isogram(word):
  my_dictionary = {}
  for x in word:
    if x in my_dictionary:
      my_dictionary[x] += 1
    else:
      my_dictionary[x] = 1
  
  for y in my_dictionary:
    if my_dictionary[y] > 1:
      return False
  return True

word = input('Enter your word:')
print(is_isogram(word))
'''




#2
'''
def find_unique(nums):
  my_dictionary = {}
  for x in nums:
    if x in my_dictionary:
      my_dictionary[x] += 1
    else:
      my_dictionary[x] = 1
   
  for y in my_dictionary:
    if my_dictionary[y] == 1:
      return y

nums = [1,2,2,3,3,4,4]
print(find_unique(nums))
'''




#3
'''
def find_unique(nums):
  result = []
  my_dictionary = {}
  for x in nums:
    if x in my_dictionary:
      my_dictionary[x] += 1
    else:
      my_dictionary[x] = 1
   
  for y in my_dictionary:
    if my_dictionary[y] == 1:
      result.append(y)
  return result

nums = [1,9,8,8,7,6,1,6]
print(find_unique(nums))
'''




#4
'''
def get_names(mydiction):
  mylist = []
  for x in mydiction:
    mylist.append(mydiction[x])
  return mylist

mydiction = {"ab":'bc',"cd":'ef'}
print(get_names(mydiction))
'''




#5
'''
def find_oldest(people):
  oldest_name = ''
  oldest_age = float('-inf')
  for name,age in people.items():  #.items() for key & value
    if age > oldest_age:
      oldest_age = age
      oldest_name = name
  return oldest_name

people = {"ab":1,"cd":2}
print(find_oldest(people))
'''




#6
'''
def letter_count(word):
  my_dictionary = {}
  for letter in word:
    if letter in my_dictionary:
      my_dictionary[letter] += 1
    else:
      my_dictionary[letter] = 1
  return my_dictionary

word = input()
print(letter_count(word))
'''




#7 positive infinity
'''
def min_grade(exams):
  lowest_course = ''
  lowest_grade = float('inf')    # Set to positive infinity
  for course,grade in exams.items():
    if grade < lowest_grade:
      lowest_grade = grade
      lowest_course = course
  return lowest_course

exams = {'a':1,'b':2,'c':3}
print(min_grade(exams))
'''




#8 positive infinity
'''
def find_youngest(people):
  you_name = ''
  you_age = float('inf')    # Set to positive infinity
  for name,age in people.items():
    if age < you_age:
      you_age = age
      you_name = name
  return you_name

people = {"ab":1,'bc':2,'cd':3}
print(find_youngest(people))
'''




#9
'''
receipt = {}
receipt['Side Salad'] = 6
receipt['Chicken Parm'] = 12
receipt['Cookie'] = 3

def mycost(receipt):
  cost = 0
  for x in receipt:
    cost += receipt[x]
  return cost

print(mycost(receipt))
'''




#10
'''
menu = {}
menu['burger'] = 10
menu['fries'] = 4
menu['soda'] = 3

def mycost(menu):
  result = []
  for x in menu:
    result.append(f'{x} cost {menu[x]}')
  return '\n'.join(result)

print(mycost(menu))
'''




#11
'''
def count_repetitions(elements):
  my_dictionary = {}
  for x in elements:
    if x in my_dictionary:
      my_dictionary[x] += 1
    else:
      my_dictionary[x] = 1
  return my_dictionary

elements = ['a','a','b','a','c','b']
print(count_repetitions(elements))
'''




#12
'''
def items_purchase(store,wallet):
  afford_list = []
  for x in store:
    if store[x] <= wallet:    #=
      afford_list.append(x)
  return afford_list

store = {'a':10,'b':50,'c':20} 
wallet = float(input('Enter the amount of money you have: '))
print(items_purchase(store,wallet))
'''




#13
'''
def total_sales(sales):
  count = 0
  for x in sales:
    count += sales[x]
  return count

sales = {'l':5,'p':10}
print(total_sales(sales))
'''




#14
'''
def high_earners(employees,salary):
  high_earners_list = []
  for x in employees:
    if employees[x] > salary:    
      high_earners_list.append(x)
  return high_earners_list

employees = {'a':1000,'b':5000,'c':2000} 
salary = float(input('Enter the amount of money you have: '))
print(high_earners(employees,salary))
'''




#15
'''
def total_donations(donations):
  count = 0
  for x in donations:
    count += donations[x]
  return count

donations = {'l':5,'p':10}
print(total_donations(donations))
'''




#16
'''
def total_calories(fruit):
  calories = {'apple':95,'banana':105,'orange':62,'grape':3,'pear':102}
  count = 0
  for x in fruit:
    count += calories[x]
  return count

fruit = ['apple','banana','orange']
print(total_calories(fruit))
'''




#17
'''
def total_cost(goods):
  prices = {'flour':2.50,'sugar':1.80,'eggs':3.00,'butter':2.75,'vanllia':4.50,'chocolate':5.00}
  count = 0
  for x in goods:
    count += prices[x]
  return count

goods = ['eggs','eggs','flour','sugar']
print(total_cost(goods))
'''




#18
'''
def majority_elment(nums):
  result = []
  my_dictionary = {}
  for x in nums:
    if x in my_dictionary:
      my_dictionary[x] += 1
    else:
      my_dictionary[x] = 1
  
  for y in my_dictionary:
    if my_dictionary[y] > len(nums)/2:
      result.append(y)
  return result

nums = [3,2,3]
print(majority_elment(nums))
'''