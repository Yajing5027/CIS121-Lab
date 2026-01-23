human_age = float(input('Enter your age: '))

# dog
dog_age = human_age*7
age = dog_age

years = int(age)

month = (age % 1)*12
months = int(month)

days = int( (month % 1) * 30)

print(f'Your age in dog years is {years:.1f} years {months:.1f} months {days:.1f} days.')

# cat
cat_age = human_age * (1/9)
age = cat_age

years = int(age)

month = (age % 1)*12
months = int(month)

days = int( (month % 1) * 30)

print(f'Your age in cat years is {years:.1f} years {months:.1f} months {days:.1f} days.')

# horse
horse_age = 3*( ( (human_age**2)-47) / 7 + 12)
age = horse_age

years = int(age)

month = (age % 1)*12
months = int(month)

days = int( (month % 1) * 30)

print(f'Your age in horse years is {years:.1f} years {months:.1f} months {days:.1f} days.')
