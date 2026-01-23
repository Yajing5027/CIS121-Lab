'''
def every_word(sentence):
  word = []
  collection = ''
  for x in sentence:
    if x != ' ':
      collection += x
    else:
      word.append(collection)
      collection = ''
    
  if collection != '':
    word.append(collection)

  return word

sentence = input('Enter your sectence:')

print(every_word(sentence))
'''


#simplified version: string.split(separator, max_split_times)
'''
def every_word(sentence):
  return sentence.split()   #string.split(separator, max_split_times)

sentence = input('Enter your sectence:')

print(every_word(sentence))
'''



'''
def every_word(sentence):
  word = []
  collection = ''
  vowel = 0
  for x in sentence:
    if x != ' ':
      collection += x
      if x in 'aeiou':
        vowel += 1
    else:
      if vowel >= 2:
        word.append(collection)
      collection = ''
      vowel = 0

  if collection != '' and vowel >=2:    #for last word
    word.append(collection)

  return word

sentence = input('Enter your sectence:')

print(every_word(sentence))
'''