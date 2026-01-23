#1
'''
while True:
    try:
        user_input = input('Please enter a number:')
        value = float(user_input)
        print(10 / value)       # notice
        break
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
'''





#2
'''
while True:
    try:
        fruit = ['apple', 'banana', 'cherry', 'date']
        user_input = input('Enter an index:')
        value = int(user_input)
        print(fruit[value])
        break
    except ValueError:
        print('Invalid index format.')
    except IndexError:
        print('Index out of range.')
'''





#3
'''
while True:
    try:
        products = {'apple': 1.5, 'banana': 0.9, 'cherry': 2.2}
        user_input = input('Enter product name:')
        if not user_input:      # notice
            print('Please enter a product name.')
            continue
        print(products[user_input])
        break
    except KeyError:
        print('Product not found.')
'''




#4
'''
while True:
    try:
        user_input = input("Enter file name:")
        with open(user_input, 'r') as f:        # notice
            print(f.read())
        break
    except FileExistsError:
        print("File not found.")
'''





#5
'''
while True:
    try:
        student = {'Alice':90, 'Bob':75, 'Charlie':60}
        user_input = input('Enter student name:')
        ex_credits = input('Enter number to add:')
        credits = float(ex_credits)
        print(student[user_input] + credits)
        break
    except KeyError:
        print("Student not found.")
    except ValueError:
        print("Invalid number.")
'''





#6
'''
while True:
    try:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        user_input = input('Enter a number:')
        day = int(user_input)
        print(week[day])
        break
    except ValueError:
        print('Invalid input.')
    except IndexError:
        print('Index out of range.')
'''





#7
'''
while True:
    try:
        num1_input = input("Enter first number:")
        num2_input = input("Enter second number:")
        num1 = int(num1_input)
        num2 = int(num2_input)
        print(f"Difference: {num1 - num2}, Ratio: {num1 / num2}")
        break
    except ValueError:
        print("Invalid input.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except OverflowError:
        print("Result too large.")
'''





#8
'''
while True:
    try:
        color = ['red', 'green', 'blue', 'yellow', 'purple']
        user_input = input("Enter an index:")
        index = int(user_input)
        print(color[index])
        break
    except ValueError:
        print("Invalid input. Try again.")
        continue
    except IndexError:
        print("Index out of range. Try again.")
        continue
'''





#9
'''
while True:
    try:
        country = {'US': 'United States', 'FR': 'France', 'JP': 'Japan', 'BR': 'Brazil'}
        user_input = input("Enter a country code:")
        print(country[user_input])
        break
    except KeyError:
        print("Code not found. Try again.")
        continue
'''





#10
'''
while True:
    try:
        prize = input("Enter prize amount:")
        num = input("Enter number of winners:")
        prize1 = float(prize)
        num1 = int(num)
        print(prize1 / num1)
        break
    except ValueError:
        print("Invalid input. Try again.")
        continue
    except ZeroDivisionError:
        print("Must have at least one winner. Try again.")
        continue
'''