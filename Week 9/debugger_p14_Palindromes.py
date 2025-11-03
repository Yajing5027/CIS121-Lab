def palindromes(words):
   # result = {"palindrome": [], "non=palindrome": []}		
   result = {"palindrome": [], "non-palindrome": []}
   
   # reversed_word = ''		
   for word in words:        
       reversed_word = ''
       #reverse the word and check if it is the original word
       for letter in word:
           reversed_word = letter + reversed_word
       # if reversed_word == word:		
       #     result["non-palindrome"].append(word)
       # else:
       #     result["palindrome"].append(word)
       if reversed_word == word:
           result["palindrome"].append(word)
       else:
           result["non-palindrome"].append(word)
   
   return result

print(palindromes(['madam','racecar','hello','level','python']))
