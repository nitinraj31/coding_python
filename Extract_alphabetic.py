# Write a python function that takes a string as input and returns a new string containing only the alphabetic characters from the original string.

def extract_alphabetic(input_string):
    result = ''.join(char for char in input_string if char.isalpha())
    return result

# Test the function
if __name__ == "__main__":
    test_string = "Hello123 World!@#"
    print(extract_alphabetic(test_string))  # Output: HelloWorld
    