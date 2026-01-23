#
word = 'Hello world'
count = 0
for x in word:
    if x !=' ':
      count += 1
print(count)


#
word_element = {'hello world','apple and bananas','happy times'}
vowel = ['a','e','i','o','u','y']
for word in word_element:
  count = 0
  for x in word:
    if x in vowel:
      count += 1
  print(f'The vowel count in {word} is {count}.')



#function take an int add two, mutiples by 4

def function(number):
  number += 2
  number *= 4
  return number
print(function (10))


#function
def function(number):
  number += 2
  number *= 4
  return number

def add_ten(number):
  number += 10
  return number

print(add_ten(function(10)))



#control 2 value
def product(num1, num2):
  product = num1 * num2
  return product
print(product(4,3))





#list and insert

lyst=['aa','bb',3,False,4.5,'cc']
print(lyst[0])
print(lyst[2:5])

#list.append(element) will add element to the end
lyst.append('dd')
print(lyst)

#list.insert(0,element) will add element to the start
lyst.insert(0,'ss')
print(lyst)

#list.insert(len(list)//2,element) will add element to right in the middle
lyst.insert(len(lyst)//2,'mm')
print(lyst)