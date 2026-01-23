income = float(input('Enter the amount of income you earned in 2023: '))
print('Are you married or single?')
state = input('Type m for married and s for single: ')

if state == 'm':
    if 0 <= income <= 11000:
        print(f'This year you owe {income*0.1} in tax.')
    elif 11001 <= income <= 44725:
        print(f'This year you owe {income*0.12} in tax.')
    elif 44726 <= income <= 95375:
        print(f'This year you owe {income*0.22} in tax.')
    else:
        print(f'Exceed.')
else:
    if 0 <= income <= 22000:
        print(f'This year you owe {income*0.1} in tax.')
    elif 22001 <= income <= 89450:
        print(f'This year you owe {income*0.12} in tax.')
    elif 89451 <= income <= 190750:
        print(f'This year you owe {income*0.22} in tax.')
    else:
        print(f'Exceed.')