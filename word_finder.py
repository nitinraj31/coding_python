a=int(("Number of words in the list :"))
for i in range(a):
    b=input("Enter the word :")
    if len(b) > 2:
        print(b[0:2] + b[-2:])
    else:
        print(b)