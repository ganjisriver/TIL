numbers = [10, 24, 31, 25, 30, 20, 1, 5, 7]

numbers[0] = 22
print(numbers)

numbers[0] = 'hello'
print(numbers)
numbers[2:4] = ['b', 'i', 'g']
print(numbers)
del numbers[2:7]
print(numbers)