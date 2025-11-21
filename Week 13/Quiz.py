#1
'''
import random
with open("Week 13/quiz_file.txt",'w') as quiz_file:
    for _ in range(100):
        random_num = random.randint(50,100)
        quiz_file.write(str(random_num)+'\n')
'''




#2
'''
file_content = []
with open("Week 13/this_file.txt","w") as this_file:
    for i in range(10):
        this_file.write(str(i)+'\n')

with open("Week 13/this_file.txt","r") as this_file:
    for row in this_file:
        file_content += row

with open("Week 13/that_file.txt","w") as that_file:
    for i in file_content:
        that_file.write(str(i))     # don't add '\n'
'''   




#3
'''
with open("Week 13/MyName.text",'w') as f:
    f.write('Matt Priem')


with open("Week 13/MyName.text",'r') as f:
    for x in f:
'''




#7
'''
total_visitors = 0
total_days = 0
with open('Week 13/LibraryVisits.csv', "r") as daily_visits:
    for row in daily_visits:
        row_items = row.split(",")
        total_visitors += int(row_items[1])
        total_days += 1
result = total_visitors//total_days
print(result)
'''



