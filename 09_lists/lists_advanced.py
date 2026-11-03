# Copying
# Assignment
import copy
letters = ['a', 'b', 'c']
letters_copy = letters  # same memory address
letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)

letters = ['a', 'b', 'c']
# .copy() - shallow copy - inner values points same memory address
letters_copy = letters.copy()
letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)

matrix = [
    ['a', 'b'],     # Row 1
    ['c', 'd']      # Row 2
]
matrix_copy = matrix.copy()
matrix[0].append('z')  # adds 'z' both of them
print('Original:', matrix)
print('Copy:    ', matrix_copy)

# Accurate and full copy which datas will be copy separatyle and different memory addresses
# Needs to import copy and use as assign copy.deepcopy(list_name)
matrix = [
    ['a', 'b'],     # Row 1
    ['c', 'd']      # Row 2
]
matrix_copy = copy.deepcopy(matrix)
matrix[0].append('z')
print('Original:', matrix)
print('Copy:    ', matrix_copy)

original = [
    ['a', 'b'],     # Row 1
    ['c', 'd'],     # Row 2
]

# Assignment
copy1 = original
print("Same Object?", original is copy1, "\n")

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Values?", original[0] is copy2[0], "\n")

# Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Values?", original[0] is copy3[0], "\n")

# Combining
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combine = letters + numbers
print(combine)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combine = [letters, numbers]
print(combine)

# Combine using .extend(list_name)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)

# Zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
combine = list(zip(letters, numbers, 'Hi'))
print(combine)

ids = [100, 101, 102, 103, 104]
names = ['Ali', 'Sara', 'John', 'Jack', 'Michael']
print(list(zip(ids, names)))

# Iterable
letters = ['a', 'b', 'c']
new_list = []
for i in letters:
    new_list.append(i.upper())
    print(new_list)

letters = ['a', '', 'c']
for index, value in enumerate(letters):
    print(index, value)

letters = ['a', 'b', 'c']
for l in reversed(letters):
    print(l)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for l, n in zip(letters, numbers):
    print(l, n)

# Map Function
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = [' Maria ', 'John ', ' Kumar']
for n in map(str.strip, names):
    print(n)

# Filter
letters = ['a', '', None, 'b', False, 'c']
print(list(filter(None, letters)))
print(list(filter(bool, letters)))

items = ['sql', '123', 'python', '1a']
print(list(filter(str.isalpha, items)))
for item in filter(str.isalpha, items):
    print(item)

# Lambda
# fmt: off
multiple = lambda x: x * 2
# fmt: on

print(multiple(2))

add = lambda x, y: x + y
print(add(2, 3))

check = lambda x: x in 'python'
print(check('h'))

prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

print(list(filter(lambda row: row[1] >= 70, students)))

# Lambda Challenge
# Keep only students with names starting with 'M'
print(list(filter(lambda row: row[0].startswith('M'), students)))

# Comprehension
domains = [
    'www.google.com',
    'openai.com',
    'localhost',
    'WWW.DATAWITHBARAA.COM'
]

cleaned = [
    # Filter - No Transformations
    d
    for d in domains
    if '.' in d
]
print(cleaned)

cleaned = [
    # Data Transformation
    d.lower().replace('www.', '')
    for d in domains

    # Data Filtering
    if '.' in d
]
print(cleaned)
