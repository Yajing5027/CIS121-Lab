#1
'''
if my_var % 2 == 1:   # Positive odd number
    if my_var ** 3 != 27:   # Cube not equal to 27, meaning not equal to 3
        my_var = my_var + 4   # Positive odd number not equal to 3 → Assignment 1 《5》9 
    else:   # Equal to 3
        my_var /= 1.5         # Assignment 2 《3》4.5
else:   # Positive even number / Negative number
    if my_var <= 10:   # 10 / Positive even number less than 10 / All negative numbers
        my_var *= 2           # Assignment 3 《10》20
    else:   # Even number greater than 10
        my_var -= 2           # Assignment 4 《12》10
print(my_var)
'''

#2
'''
(a) has two independent parts. You can go to part A and also go to part B if both are true.
(b) has one part with two branches. If A is true, you go to A side. If A is not true, then you check B side.
'''

#3
'''
light_color = input('Enter the color: ')

if light_color == "red":
    print('stop')
elif light_color == "green":
    print('go')
elif light_color == 'yellow':
    print('yield')
else:
    print('Invalid')
'''

#4
'''
age = int(input('Enter your age: '))
goal = input('Enter your athleticism goal: ')

if 20 <= age <= 39:
    if goal == 'Above Average':
        print(f'Your resting heart rate should be between 47-72')
    else :
        print(f'Your resting heart rate should be between 73-93')
elif 40 <= age <= 59:
    if goal == 'Above Average':
        print(f'Your resting heart rate should be between 46-71')
    else :
        print(f'Your resting heart rate should be between 72-94')
elif 60 <= age <= 79:
    if goal == 'Above Average':
        print(f'Your resting heart rate should be between 45-70')
    else :
        print(f'Your resting heart rate should be between 71-97')
'''

#5
'''
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(c,b,a)
    elif c > a:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if a > c:
        print(c,a,b)
    elif c > b:
        print(a,b,c)
    else: 
        print(a,c,b)
'''
# Improved version (variable swapping)
'''
a = int(input())
b = int(input())
c = int(input())

if a>b:
    a,b = b,a
if a>c:
    a,c = c,a
if b>c:
    b,c = c,b
print(a,b,c)
'''

#6
'''
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(a, b, c)
    elif c > a:
        print(c, a, b)
    else:
        print(a, c, b)
else:
    if a > c:
        print(b, a, c)
    elif c > b:
        print(c, b, a)
    else: 
        print(b, c, a)
'''
# Improved version (variable swapping)
'''
a = int(input())
b = int(input())
c = int(input())

if a<b:
    a,b = b,a
if a<c:
    a,c = c,a
if b<c:
    b,c = c,b
print(a,b,c)
'''

#7
'''
knuts_input = int(input('Enter knuts amount:'))

if knuts_input >= 29:
    sickles = knuts_input // 29
    k = knuts_input % 29
    if sickles >= 17:
        galleon = sickles // 17
        s = sickles % 17
        if s > 0 and k > 0:
            print(f'Given {knuts_input} knuts, output {galleon} galleons {s} sickles {k} knuts.')
        elif s > 0:
            print(f'Given {knuts_input} knuts, output {galleon} galleons {s} sickles.')
        else:
            print(f'Given {knuts_input} knuts, output {galleon} galleons {k} knuts.')
    else:    
        if k > 0:
            print(f'Given {knuts_input} knuts, output {sickles} sickles {k} knuts.')
        else:
            print(f'Given {knuts_input} knuts, output {sickles} sickles.')
else:
    print(f'Given {knuts_input} knuts, output {knuts_input} knuts.')
'''
#8
'''
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(f'The largest number is {a}.')
    elif c > a:
        print(f'The largest number is {c}.')
    else:
        print(f'The largest number is {a}.')
else:
    if a > c:
        print(f'The largest number is {b}.')
    elif c > b:
        print(f'The largest number is {c}.')
    else: 
        print(f'The largest number is {b}.')
'''

#9
'''
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(f'The smallest number is {c}.')
    elif c > a:
        print(f'The smallest number is {b}.')
    else:
        print(f'The smallest number is {b}.')
else:
    if a > c:
        print(f'The smallest number is {c}.')
    elif c > b:
        print(f'The smallest number is {a}.')
    else: 
        print(f'The smallest number is {a}.')
'''
#10

#11
from random import randint

coin = randint(0, 1)   
guess = input("Guess Heads or Tails: ")

if coin == 0:
    result = "Heads"
else:
    result = "Tails"

if guess == result:
    print("Correct.", result)
else:
    print("Incorrect.", result)


#12
'''
a = int(input('Pick a number: '))
b = int(input('Pick another number: '))
c = int(input('Pick another number: '))

if a == b or a == c:
    if b == c:
        print(f'You enterd the same number 3 times.')
    else: 
        print(f'You enterd the same number 2 times.')
elif b == c:
        print(f'You enterd the same number 2 times.')
else:
    print(f'each number is unique.')
'''

#13
'''
highway = int(input('Pick a highway number: '))

if 0 <= highway <= 99:
    if highway % 2 == 1:
        print(f'highway {highway} runs north/south.')
    else:
        print(f'highway {highway} runs east/west.')
elif 100 <= highway <= 999:
    a = highway % 100                                       #reminder express
    if a == 0:
        print('Invalid highway number.')
    elif a % 2 == 1:
        print(f'highway {highway} runs north/south.')
    else:
        print(f'highway {highway} runs east/west.')
else:
        print('Invalid highway number.')
'''

#17
'''
player_1 = input('Player 1 choice: ')
player_2 = input('Player 2 choice: ')

if player_1 == 'Rock':
    if player_2 == 'Rock':
       print("It's a tie!") 
    elif player_2 == 'Paper':
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')
elif player_1 == 'Paper':
    if player_2 == 'Rock':
       print('Player 1 wins!') 
    elif player_2 == 'Paper':
        print("It's a tie!")
    else:
        print('Player 2 wins!')
elif player_1 == 'Scissors':
    if player_2 == 'Rock':
        print('Player 1 wins!') 
    elif player_2 == 'Paper':
        print('Player 2 wins!')
    else:
        print("It's a tie!")
else:
    print('Invalid')
'''


#18
'''
a = int(input('Pick side length 1: '))
b = int(input('Pick side length 1: '))
c = int(input('Pick side length 1: '))

if a == b or a == c:
    if b == c:
        print(f'equilateral triangles.')
    else: 
        print(f'isosceles triangles.')
elif b == c:
        print(f'isosceles triangles.')
else:
    print(f'scalene triangles.')
'''

#19
'''
name = input('Enter the name: ')
if name == 'Darth Vader':
    print(f'Father')
elif name == 'Leia':
    print(f'Sister')
elif name == 'Han':
    print(f'Brother in law')
elif name == 'R2D2':
    print(f'Droid')
else:
    print(f'unknow')
'''
