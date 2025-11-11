# write a python program to take input from user and store in list and find odd and even numbers in the list and store them in separate lists
# and print the lists
# Taking input from user
user_input = input("Enter numbers separated by spaces: ")
# Splitting the input string into a list of numbers (as strings)    
num_list = user_input.split()
# Initializing empty lists for odd and even numbers
odd_numbers = []
even_numbers = []
# Iterating through the list of numbers
for num_str in num_list:
    num = int(num_str)  # Converting string to integer
    if num % 2 == 0:
        even_numbers.append(num)  # Appending to even numbers list
    else:
        odd_numbers.append(num)   # Appending to odd numbers list
# Printing the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
# # Write a Python program to find all numbers between 1000 and 3000 (both included) such that each digit of the number is even, and then print them in a single line separated by commas.
# even_numbers_range = []
# for num in range(1000, 3001):
#     str_num = str(num)
#     if all(int(digit) % 2 == 0 for digit in str_num):
#         even_numbers_range.append(str_num)
# print(",".join(even_numbers_range))
