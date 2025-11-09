# Write a program to remove all vowels from a string. 
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch not in vowels:
        result += ch
print("String without vowels:", result)
