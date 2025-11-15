# Write a program in python l[p through the list and classify each score and "pass" or "fail " (passing marki s 50 ).
# Store the result in a new list of dictionaries with keys :- "Score " and "Status ".

def classify_scores(scores):
    # New list to store results
    result = []
    # Loop through each score
    for score in scores:
        # Classify as pass or fail
        status = "pass" if score >= 50 else "fail"
        # Create dictionary
        entry = {"Score": score, "Status": status}
        # Append to result list
        result.append(entry)
    return result

# Test cases
test_cases = [
    [45, 55, 30, 70, 49, 60, 25, 80],  # Original
    [50],  # Exactly 50
    [-10, 0, 49.9],  # Negative, zero, below 50 float
    [100, 150],  # High scores
    [49.5, 50.5],  # Floats
    [],  # Empty list
    [50, 50, 49, 49]  # Duplicates
]

for i, scores in enumerate(test_cases):
    print(f"Test case {i+1}: {scores}")
    result = classify_scores(scores)
    print(result)
    print()
