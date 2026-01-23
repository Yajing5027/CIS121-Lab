#1
'''
lar_num = int(input('Enter a number: '))
sma_num = int(input('Enter a number: '))

if lar_num < sma_num:
  lar_num,sma_num = sma_num,lar_num   # = for swap 2 variable; == for compare 2 value

halved = lar_num/2
result = 0
squence = str(lar_num)    #set a string

while halved > sma_num:
  result += 1
  squence += ' -> ' + str(halved)   #change number to string, connect strings
  halved /= 2
print(f'if larger = {lar_num} and smaller = {sma_num}, the result should be {result}, since {squence}.')
'''




#2
'''
user_word = input('Enter your letter: ')
squence = ''

for x in user_word[1:len(user_word):2]:   #attention that start is 1 not 2, the first is 0
  squence += x

print(squence)
'''




#3 range(start, stop, step)
'''
for x in range(37+1, 1050+1, 2):
  print(x)
'''




#4 string connect
'''
word = ''   #initialize empty string

while True:
  user_let = input('Enter an litter (or type done): ')
  
  if user_let == 'done':
    break
  else:
     word += user_let   #unlimit on number, also can connect strings

print(word)
'''




#5 accumulator：total=0
'''
total=0
for x in range(50+1, 517+1, 2):
  total += x    #total = total + x
  #print(total)  inside: every time print
print(total) #outside: only finally print
'''




#6 Bull loop: while <condition> + <condition> flase
'''
total = 0
user_num = int(input('Enter your integer:'))    #start input for while judge

while user_num >= 0:
  total += user_num
  user_num = int(input('Enter your integer:'))    #continue input in loop

print(total)
'''
#6 Bull loop: while True + break
'''
total = 0

while True:
  user_num = int(input('Enter your integer:'))
  
  if user_num < 0:
    break
  else:
    total += user_num

print(total)
'''




#7
'''
n=25
squence = str(n)    #strat at n

while n != 1:
  if n % 2 == 0:
    n /= 2
  else:
    n = n*3 + 1
  squence += ' -> ' + str(int(n))   #remove float
print(squence)
'''




#8
'''
user_num = int(input('Enter a number: '))
squence = ''

for x in range(1,user_num+1):
  if user_num % x == 0:       #needn't else
    squence += ' ' + str(x)

print(squence)
'''




#9
'''
width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a pattern: ')

print('Your rug is:')

len_width = ''

for w in range(1,width+1):    #w times pattern be added to len_width
    len_width += pattern

for l in range(1,length+1):
  print(len_width)
'''
#9 Improved version: string can directly * each other
'''
width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a pattern: ')

print('Your rug is:')

for x in range(1,length+1):
  print(pattern * width)
'''




#10
'''
user_num = int(input('Enter a number: '))
largest = 0

while user_num >= 0:
  if user_num % 2 == 0 and user_num > largest:
    largest,user_num = user_num,largest
  user_num = int(input('Enter a number: '))

if largest == 0:
  largest = -1    #set value use =

print(f'largest = {largest}')
'''




#11
'''
user_num = int(input('Enter a number: '))
squence = '1^2'
total = 1

for x in range(2,user_num+1):
  squence += ' + ' + str(x) + '^2'    #^2 is a str so add''
  total += x**2

print(f'if user_number = {user_num}, the result should be {total}, since {squence} = {total}.')
'''