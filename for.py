
n = int(input("How many numbers do you want to average? "))

# Initialize sum to 0
total = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num  # Add to total

# Calculate average
average = total / n

# Print the result
print("Average of all numbers:", average)
