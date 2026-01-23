x = int(input('Enter your stardand number: '))
if x>57:
    print(f'Please enter the right number.')
elif x>=51:
    if x==57:
        print('A+')
    elif x>=53:
        print('A')
    else:
        print('A-')
elif x>=45:
    if x>=49:
        print('B+')
    elif x>=47:
        print('B')
    else:
        print('B-')
elif x>=40:
    if x>=43:
        print('C+')
    else:
        print('C')
elif x>=35:
    print('D') 
else:
    print('F')