def Saize(sentence, word):
     
    # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
 
        if (i == word):
            return True
    return False

s = "Mohammad Saize Ali"
word = "Ali"
 
if (Saize(s, word)):
    print("Yes")
else:
    print("No")