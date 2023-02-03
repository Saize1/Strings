str1 = input('Enter a string: ')
#converting the characters of string into a set elements to remove dublicacy.
#use join() function to join all the remaining set elements together.
result="".join(dict.fromkeys(str1))
print(result)