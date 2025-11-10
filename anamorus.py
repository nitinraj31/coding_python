# Write a program to remove all vowels from a string. 
a=input("Enter the string :")
b=""
for char in a:
    if char not in "aeiouAEIOU":
        b+=char
print("String after removing vowels :",b)
# Example input: "Hello World"
# Example output: "Hll Wrld"