numbers=[10,20,30,40]
print(numbers[0:2])  # Output: [10, 20]
print(numbers[1:3])  # Output: [20, 30]
print(numbers[2:4])  # Output: [30, 40]
print(numbers[:3])   # Output: [10, 20, 30]
print(numbers[3:])   # Output: [40]
print(numbers[-2:])  # Output: [30, 40]
print(numbers[-2:])  # Output: [30, 40]
print(numbers[3:])  # Output: [40]
print(numbers[::2])  # Output: [10, 30]


print(len(numbers))  # Output: 4

print(max(numbers))  # Output: 40
print(min(numbers))  # Output: 10
print(sum(numbers))  # Output: 100

print(sorted(numbers))  # Output: [10, 20, 30, 40]
print(sorted(numbers, reverse=True))  # Output: [40, 30, 20, 10]
print(any(num > 25 for num in numbers))  # Output: True
print(all(num > 5 for num in numbers))  # Output: True
fruits = ['apple', 'banana', 'cherry']
index = 1
print(index, fruits)


name=["babli","nitin","shubham","kunal "]
for name,mark in zip(name,numbers):
    print(name,mark)    