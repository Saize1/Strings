string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = 1
        break

if(count == 0):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ", char, " is Found at Position " , count+ 1)