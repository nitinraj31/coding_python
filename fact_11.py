n=int(input("Enter a number to find its factorial:  "))
fact =1
i=1
if n<0:
    print("Factorial does not exist for negative number ")
elif n==0:
    print("the factorial of 0 is 1")
else:
    while i<=n:
        fact=fact*i
        i=i+1
    print("the factorial of",n,"is",fact)