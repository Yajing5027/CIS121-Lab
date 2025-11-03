def return_unique(numbers):

   number_dicitonary = {}
   # for number in range(len(numbers)):   
   for number in numbers:
       if number in number_dicitonary:
           # number_dicitonary[number] = 1   
           number_dicitonary[number] += 1
       else:
           number_dicitonary[number] = 1

   unique_numbers = []
   # for number in number_dicitonary.values(): 
   for number in number_dicitonary:
       if number_dicitonary[number] == 1:
           unique_numbers.append(number)

   return unique_numbers