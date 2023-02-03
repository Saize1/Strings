string = "Mohammad Saize Ali"
  
# frequency dictionary
freq = {} 
    
for element in string: 
    if element in freq: 
        freq[element] += 1
    else: 
        freq[element] = 1
    

print ("Occurrence of all characters in Mohammad Saize Ali is :\n "+ str(freq)) 