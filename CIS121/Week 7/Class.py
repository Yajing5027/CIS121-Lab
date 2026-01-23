# add key:value & add value count in dictionary
def letter_counter(word):

  word = word.replace(' ','')   #string.replace('old', 'new') notice to use parentheses

  letter_dictionary = {}
  for letter in word:
    if letter in letter_dictionary:
      letter_dictionary[letter] += 1    #add value count
    else:
      letter_dictionary[letter] = 1   #add key:value
  return letter_dictionary

word = 'peter piper picked a peck of pickled pepper'
print(letter_counter(word))