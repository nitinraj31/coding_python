name=["Alice","Nitin","Aman","Anushka"]
C_name=[name for name in name if name .startswith('N')]
print(C_name)
A_name=[name for name in name if name .startswith('A')]
print(A_name)
# Write a Python program to take a list of names and filter out those that start with the letter 'A' and 'N' respectively. Print the filtered lists.
# Example Output:
# Names starting with 'N': ['Nitin']    
# Names starting with 'A': ['Alice', 'Aman', 'Anushka']
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = [name for name in names if name.startswith('N')]
# names_starting_with_A = [name for name in names if name.startswith('A')]
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = []
# names_starting_with_A = []
# for name in names:
#     if name.startswith('N'):
#         names_starting_with_N.append(name)
#     elif name.startswith('A'):
#         names_starting_with_A.append(name)
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]

# names_starting_with_N = list(filter(lambda name: name.startswith('N'), names))
# names_starting_with_A = list(filter(lambda name: name.startswith('A'), names))
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = []
# names_starting_with_A = []
# for name in names:
#     if name[0] == 'N':
#         names_starting_with_N.append(name)
#     elif name[0] == 'A':
#         names_starting_with_A.append(name)
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = [name for name in names if name[0] ==
#                         'N']
# names_starting_with_A = [name for name in names if name[0] == 'A']
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = []
# names_starting_with_A = []
# for name in names:
#     if name.lower().startswith('n'):
#         names_starting_with_N.append(name)
#     elif name.lower().startswith('a'):
#         names_starting_with_A.append(name)
# print("Names starting with 'N':", names_starting_with_N)
# print("Names starting with 'A':", names_starting_with_A)
# names = ["Alice", "Nitin", "Aman", "Anushka"]
# names_starting_with_N = [name for name in names if name.lower().startswith('n')]
# names_starting_with_A = [name for name in names if name.lower().startswith('a')]
# print("Names starting with 'N':", names_starting_with_N)
