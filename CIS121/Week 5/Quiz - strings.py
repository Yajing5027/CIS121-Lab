#1 negitive index
'''
def reverse_string(word):
  return word[-1:-len(word)-1:-1]   #step lose -> step = +1
# word[-1:-len(word)-1:-1] can simplified as word[::-1]
'''
'''
 h     e     l     l     o
 0     1     2     3     4      len(word): positive index
-5    -4    -3    -2    -1     -len(word): negitive index

-len(word)   -> 'h'
-len(word)-1 -> 'h'-1
'''
'''
word = input('Enter your word: ')

print(f'word in reversed order is {reverse_string(word)}.')
'''




#2
'''
def is_fever(fever):
  result = ''
  value = float(fever[0:-1])    #first one to last one #don't lose float!!
  if fever[-1] == 'F':    #last one
    if value > 98.6 :
      result = True
    else:
      result = False
  else:
    if value > 37:
      result = True
    else:
      result = False

  return result

fever = input('Enter a temperature 00F or 00C: ')

print(f'is fever {is_fever(fever)}.')
'''
#2 simplify version: value_if_true if condition else value_if_false
'''
def is_fever(fever):
  value = float(fever[0:-1])
  return (value >98.6) if fever[-1] == 'F' else (value >37)

fever = input ('Enter your temperature 00F or 00C: ')

print(f'is fever {is_fever(fever)}')
'''




#3
'''
def is_boiling(temp):
  if temp[-1] == 'F':
    return True if float(temp[0:-1])>=212 else False
  else:
    return True if float(temp[0:-1])>=100 else False
  
temp = input('Enter temperature: ')
print(is_boiling(temp))
'''




#4
'''
def hamming_distance(string_1,string_2):
  count = 0
  for index in range(0,len(string_1)):    #no +1, range stops before len, last index already included
    if string_1[index] != string_2[index]:
      count += 1
  return count

string_1 = input('Enter string_1: ')
string_2 = input('Enter string_2: ')
print(hamming_distance(string_1,string_2))
'''




#5
'''
def is_isogram(word):
  for letter in word:
    if word.count(letter)>1 
      return True
  return False    #notice indentation position

word = input('Enter word: ')
print(is_isogram(word))
'''




#6
'''
def get_drink_ID(name,capacity):
  result = name[:3] + str(capacity)   #number must change to str
# or f-string: result = f'{name[:3]}{caoacity}'
  return result

name = input('Enter the name: ')
capacity = int(input('Enter the capacity: '))

print(get_drink_ID(name,capacity))
'''




#7 string.split(separator, max_split_times)
'''
def first_letters(sentence):
  word_list = sentence.split()    #string.split(separator, max_split_times)
  
  result = ''
  for word in word_list:
    result += word[0] 
    
  return result

sentence = input('Enter your sentence: ')
print(first_letters(sentence))
'''




#8
'''
def first_letters(sentence):
  word_list = sentence.split()
  
  result = ''
  for word in word_list:
    result += word[-1] 
    
  return result

sentence = input('Enter your sentence: ')
print(first_letters(sentence))
'''




#9 index of last word != len()
'''
def flip_flop(word):
  if len(word)%2 == 0:
    result = word[len(word)//2:] + word[:len(word)//2]
  else:
    result = word[len(word)//2+1:] + word[len(word)//2] + word[:len(word)//2]
  return result


word = input('Enter your word: ')

print(flip_flop(word))
'''
#9 simplified version
'''
def flip_flop(word):
  mid = len(word)//2
  odd = len(word)%2
  result = word[mid+odd:] + word[mid:mid+odd] + word[:mid]
  return result


word = input('Enter your word: ')

print(flip_flop(word))
'''