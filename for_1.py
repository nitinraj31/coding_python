n=int(input("enter numbers :"))
total=0
for i in range(n):
    num=float(input("enter number :"))
    total+=num  
average=total/n
print("Average of all numbers:", average)   