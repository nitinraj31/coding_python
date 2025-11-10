num=int(input("Enter a number:"))
fact=1
for i in range (num,num+1):
    fact*=i
    print("the factorial value of an user is ",fact)

# Write a program to remove all vowels from a string.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch not in vowels:
        result += ch
print("String without vowels:", result)