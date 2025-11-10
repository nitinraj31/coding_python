# check whether a given string is palindrome or not
a=input("Enter the string :")
b=a[::-1]
if a==b:
    print("The given string is palindrome ")
else:
    print("The given string is not palindrome ")
    