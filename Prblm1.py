# Reverse String
# Method 1
str1 = "Saize"
print("Original String is:", str1)

str1 = str1[::-1]
print("Reversed String is:", str1)

# Method 2
str1 = "Saize"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)