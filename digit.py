#Write a Python program to find all numbers between 1000 and 3000 (both included) such that each digit of the number is even, and then print them in a single line separated by commas.
even_numbers = []
for num in range(1000, 3001):
    str_num = str(num)
    if all(int(digit) % 2 == 0 for digit in str_num):
        even_numbers.append(str_num)
print(",".join(even_numbers))
