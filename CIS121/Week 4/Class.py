#loops
'''
num = 1
while num <= 10:
    print(num)
    num += 1
'''
'''
#help(range)
for num in range(1,10+1):
    print(num)
'''


#even number
'''
num = 1
while num <= 10:
    if num %2 == 0:
        print(num)
    num += 1
'''
'''
for num in range(2,11,2):
    print(num)
'''


#odd number from 5 to user give:
'''
max_num = int(input('Enter a number: '))
num = 5
while num <= max_num:
    if num %2 == 1:
        print(num)
    num += 1
'''
'''
max = int(input('Enter you number:'))
for num in range(5,max+1,2):
    print(num)
'''


#(continue) even number not%3=0
'''
num = 0
while num < 50:
    if num % 2 == 0:
        if num % 3 == 0:
            num += 1 #prevent an infinite loop
            continue
        else:
            print(num)
    num += 1
'''
'''
for num in range (2,50,2)
    if num %3 == 0:
        continue
    else:
        print(num)
'''


#stop when input is q
'''
total = 0

while True:
    user = input("Enter a number or type q to end: ")
    
    if user != 'q':      
        total += int(user)
    else:                
        break

print("Total =", total)
'''




#String slicing in Python uses a left-closed, right-open interval [start:end ).
x = 'hello world'
print(x[2:8])



