# Write a Python to Create a new list that contains only the even numbers from the original  list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in original_list if num % 2 == 0]
print("Even numbers in the list:", even_numbers)


#from taking from user in list 
n=int(input("enter the number"))
if n%2==0:
    print("even")
    even_list = []
    for i in range(2, n+1, 2):
        even_list.append(i)
    print("Even numbers from 1 to", n, "are:", even_list)
else:
    print("odd")
    print("The number is odd, cannot generate even numbers list.")
    