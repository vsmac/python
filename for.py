# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum = sum + val
    if val == 3:
        break

print("sum is:", sum)