num=int(input("Enter a numner:"))
if num <=1:
    print("not a prime no ")
else:
    for i in range (2, num):
        if num % i == 0:
            print("the user input value is not a prime numer ")
            break
    else:
        print("the value input by na user is an prime number ")
