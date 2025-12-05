#1
'''
import random
with open("QuizInts.txt",'w') as f:
    for _ in range(100):        # _ is a placeholder
        num = random.randint(50,200)
        f.write(f'{num}\n')
'''







#2 every other line
'''
with open("thisFile.txt","r") as isf:
    content = isf.readlines()
with open("thatFile.txt","w") as atf:
    for x in content[::2]:      # every other line
        atf.write(x)        # no need to add newline, since readlines keeps it
'''







#3 print each character
'''
with open("MyName.txt",'w') as f:
    f.write('Yajing Ren')
with open("MyName.txt",'r') as f:
    name = f.read().strip()     # strip removes whitespace from both ends of the line, doesn't affect inside, returns string
    for x in name:      
        print(x)
'''







#4
'''
with open('MyWords.txt','r') as mwf:
    words = [x.strip() for x in mwf.readlines()]       # strip can't be applied directly to list, only to strings, so use loop
with open('New.txt', 'w') as nf:
    for i in range(4):
        line_word = words[i*5:i*5+5]        # dynamic slicing
        line = ' '.join(line_word)
        nf.write(line + '\n')
'''

#5 Extract specific content from each line - Method 1: read file into list of lines, then split each line into list of strings, take index[1]
'''
total = 0
with open('LunchData.txt','r') as f:
    lines = f.readlines()
    for x in lines:
        # split the line by spaces
        data = x.strip().split()        # split() without args defaults to splitting by whitespace (spaces, tabs, newlines), returns list
        total += int(data[1])       # remember to convert to int; index is 1

    print(total)
'''
#5 Simpler logic: read entire file as string, then take every other value
'''
total = 0
with open('LunchData.txt','r') as f:
    data = f.read().split()
    for x in data[1::2]:        # every other one
        total += int(x)       

    print(total)
'''







#6
'''
word = {}
with open('aMorePerfectUnion.txt','r') as f:
    speech = f.read().split()
    for x in speech:
        if x in word:
            word[x]+= 1
        else:
            word[x] = 1
print(word)
'''







#7 memory-efficient loop
'''
total = 0
day = 0
with open('LibraryVisitsData.csv','r') as f:
    for x in f:
        data = x.strip().split(',')      # CSV format separated by ',', strip to handle whitespace
        total += int(data[1])     # remember to convert to int
        day += 1
    average = total / day
print(average)
'''
#7 memory-intensive readlines
'''
total = 0
with open('LibraryVisitsData.csv','r') as f:
    lines = f.readlines()
    for x in lines:
        data = x.strip().split(',')      # CSV format separated by ',', strip to handle whitespace
        total += int(data[1])     # remember to convert to int
    average = total / len(lines)
print(average)
'''







#8
'''
highest = float('-inf')
result = None
with open('CaloriesBurnedData.txt','r') as f:
    for x in f:
        data = x.strip().split()
        if int(data[1]) > highest:
            highest = int(data[1])
            result = data[0]
print(result)
'''







#9 skip header
'''
total = 0
with open('ScienceFairVisitors.txt','r') as f:
    lines = f.readlines()[1:]       # both readlines and read work
    for x in lines:
        data = x.strip().split()
        total += int(data[1])
print(total)
'''







#10 store in dictionary
'''
club = {}
with open('PagesRead.csv','r') as f:
    lines = f.readlines()[1:]
    for x in lines:
        data = x.strip().split(',')         # CSV format separated by ',', strip to handle whitespace
        club[data[0]] = int(data[1]) + int(data[2])
print(club)
'''







#11 store in dictionary
'''
user = {}
with open('SongPlays.txt','r') as f:
    lines = f.readlines()[1:]
    for x in lines:
        data = x.strip().split()
        if data[0] in user:
            user[data[0]] += int(data[1])       # remember to convert to int
        else:
            user[data[0]] = int(data[1])
print(user)
'''







#12
'''
temperature = []
highest = float('-inf')     # initialize negative infinity as highest
lowest = float('inf')       # initialize positive infinity as lowest
total = 0
with open('DailyTempera-tures.csv','r') as f:
    lines = f.readlines()[1:]
    for x in lines:
        data = x.strip().split(',')
        num = int(data[1])
        temperature.append(num)
        if num < lowest:
            lowest = num 
        if num > highest:
            highest = num
        total += num
    average = total / len(temperature)
print(f"Highest: {highest}, Lowest: {lowest}, Average: {average}")
'''







#13
'''
with open('Family.csv','w') as f:
    family = {'mom':50,'dad':50,'sister':30,'me':20}
    f.write(f'Name,Age\n')
    for name,age in family.items():     # items() has parentheses
        f.write(f'{name},{age}\n')
'''