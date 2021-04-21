# Install Homebrew, pyenv and Python3, activate venv:
# - https://opensource.com/article/19/5/python-3-default-mac
# - https://opensource.com/article/20/4/pyenv
# List all available Python versions:
# "pyenv install --list | grep " 3\.[789]"
# "pyenv install 3.9.4"
# "pyenv global 3.9.4"
# OR for particular project: "pyenv local 3.9.4"
# Create and activate virtual environment:
# "python -m venv my-project"
# "cd my-project && source ./bin/activate"
# Deactivate virtual environment:
# "deactivate"
# Install all requirements/dependencies:
# "pip install -r requirements.txt"


# Devision with rounding => 2
print(9 // 4)

# Modulo => 1
print(9 % 4)

# Constants
PI = 3.14
print(type(PI))

name = 'John'
age = 999

# Formatted string / fstring
print(f'Hello {name}, you\'re {age} years old')

# String / list slicing
# [start:stop:stepover]
selfish = '01234567'
print(selfish[1:7:2])
print(selfish[0:len(selfish)])

# Capitalize letters
quote = 'this is the truth, live by the truth'
print(quote.capitalize())
print(quote.upper())

print(bool('Trr'))

# Taking the input from a terminal
# year_of_birth = input('What\'s your year of birth?')
# print(f'Your age is: {2020 - int(year_of_birth)}')

# Working with lists
basket = ['a', 'b', 'c', 'd', 'e']

# Add the specified list elements (or any iterable) to the end of the current list
basket.extend('fg')
# Add an element to the end of the list
basket.append('bi!')
# Add an element to the beginning of the list
basket.insert(0, 'hi!')
# basket.sort()
# basket.reverse()
print(f'basket: {basket}')

# Copy a list with slicing
new_basket1 = basket[:]
# Copy a list
new_basket2 = basket.copy()


basket_sorted_reversed = list(reversed(sorted(new_basket2)))

print(f'basket_sorted_reversed: {basket_sorted_reversed}')

# Providing default values to the objects (dictionaries)
user = {
    'basket': [1, 2, 3],
    'greet': 'Wellhelooo'
}

print(user.get('age', 180))
# Update dict value
print(user.update({ 'age': 220 }))
# Add dict value
print(user.update({ 'ancient': True }))
print(user)
user.clear()
print(user)

print('Hello' == "Hello")

# Ranges - range(start, stop, step)
for digit in range(5):
    print(digit)

# Lambda functions - lambda arguments: expression
# Filter odd numbers with lambda
numbers_list1 = [5, 9, 7, 14, 97, 54, 22, 77, 83, 79, 68]
 
odd_numbers_list = list(filter(lambda x: (x % 2 != 0), numbers_list1))
print(f'odd_numbers_list: {odd_numbers_list}')

# Map to double each number in the list
numbers_list2 = [5, 9, 7, 14, 97, 54, 22, 77, 83, 79, 68]
 
doubled_numbers_list = list(map(lambda x: x * 2, numbers_list2))
print(f'doubled_numbers_list: {doubled_numbers_list}')
