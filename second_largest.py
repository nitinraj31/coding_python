# Program to find the second largest number in a list of n numbers without using sort() or sorted()

# Input the number of elements
n = int(input("Enter the number of elements (n): "))

# Check if n is at least 2
if n < 2:
    print("Please enter at least 2 numbers to find the second largest.")
else:
    # Input the numbers
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    # Initialize max1 and max2
    max1 = max2 = float('-inf')

    # Iterate through the numbers to find max1 and max2
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    # Output the result
    if max2 == float('-inf'):
        print("All numbers are the same; there is no second largest number.")
    else:
        print(f"The second largest number is: {max2}")
