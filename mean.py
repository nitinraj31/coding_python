# Write a python program 
# Use Numpy to create an array and find the mean and standard deviation .
# use pandas to create a data form with these numbers and add a new column showing weathear each number is above the mean .

import numpy as np
import pandas as pd

# Step 1: Take input from the user
numbers = input("Enter numbers separated by spaces: ")
numbers = numbers.replace(',', ' ')  # Replace commas with spaces to handle comma-separated input
numbers_list = []
for num in numbers.split():
    try:
        numbers_list.append(float(num))
    except ValueError:
        print(f"Invalid input: '{num}' is not a number. Skipping.")
if not numbers_list:
    print("No valid numbers entered. Exiting.")
    exit()

# Step 2: Convert list to NumPy array
num_array = np.array(numbers_list)

# Step 3: Compute mean and standard deviation
mean_val = np.mean(num_array)
std_dev = np.std(num_array)

print(f"\nMean of the numbers: {mean_val}")
print(f"Standard Deviation: {std_dev}")

# Step 4: Create a Pandas DataFrame
df = pd.DataFrame(num_array, columns=["Number"])

# Step 5: Add a new column showing if each number is above the mean
df["Above Mean"] = df["Number"] > mean_val

# Display the DataFrame
print("\nDataFrame:")
print(df)
