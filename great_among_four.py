a=int(input("Enter the first value:"))
b=int(input("Enter the second  value:"))
c=int(input("Enter the third value:"))
d=int(input("Enter the fourth value:"))
if((a>b) and (a>c) and (a>d)):
    print("The greatest number is:", a )
elif((b>a) and (b>c) and (b>d)):
    print("The greatest number is:", b )
elif((c>a) and (c>b) and (c>d)):
    print("The greatest number is:",c )       
else:
    print("The greatest number is:", d )   
print("The python program is executed successfully")
