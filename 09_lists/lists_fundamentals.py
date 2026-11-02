# Create List
empty = []
print(empty)
print(type(empty))

# string values
letters = ['a', 'b', 'c']
print(letters)
print(type(letters))

# integer values
numbers = [1, 2, 3]
print(numbers)
print(type(numbers))

# mixed values
mixed = ['a', 20, None, True]
print(mixed)
print(type(mixed))

# list()
empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)

# Nested List
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix)
print(type(matrix))

mixed_matrix = [
    ['abc', 'ABC'],
    [1, 2, 3, 4, 5],
    [True, False]
]
print(mixed_matrix)
print(type(mixed_matrix))

# Access & Read
# Indexing
lst = ['a', 'b', 'c', 'd']
print(lst[0])   # first value
print(lst[-1])  # last value

matrix = [
    ['a', 'b', 'c'],    # Row 0
    ['d', 'e', 'f'],    # Row 1
    ['g', 'h', 'i']     # Row 2
]
print('Show first row:', matrix[0])
print('Show first row:', matrix[-3])
print('Show last row:', matrix[2])
print('Show last row:', matrix[-1])
print('Show a:', matrix[0][0])
print('Show a:', matrix[-3][-3])
print('Show e:', matrix[1][1])
print('Show e:', matrix[-2][-2])
print('Show i:', matrix[2][2])
print('Show i:', matrix[-1][-1])

# Slicing
lst = ['a', 'b', 'c', 'd']
print(lst[:2])
print(lst[2:])
print(lst[:])
print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2])


# Asterisk (*) - List Unpacking
name, age, role, country = ['Maria', 29, 'Data Engineer', 'Spain']
print(name)
print(age)
print(role)
print(country)

# Unpack only first and last items
name, *details, country = ['Maria', 29, 'Data Engineer', 'Spain']
print(name)
print(details)
print(country)

# Unpack only first item
name, *details = ['Maria', 29, 'Data Engineer', 'Spain']
print(name)
print(details)

# Unpack only first item
*details, country = ['Maria', 29, 'Data Engineer', 'Spain']
print(details)
print(country)

first, *rest = [1]
print(first)
print(*rest)

first, *rest = "Hello"
print(first)
print(*rest)

# underscore (_)
name, _, role, _ = ['Maria', 29, 'Data Engineer', 'Spain']
print(name)
print(role)

# asterisk(*) + underscore (_)
name, *_, country = ['Maria', 29, 'Data Engineer', 'Spain']
print(name)
print(country)

# Analysis # Checks
numbers = [1, 3, 5, 5, 2, 10]
print('Max:', max(numbers))
print('Min:', min(numbers))
print('Sum:', sum(numbers))
print('Len:', len(numbers))

# True if all of list items are not empty or not zero
print('All:', all(numbers))
print('All:', all([1, 0, 2]))
print('All:', all(['a', 'b', 'c']))
print('All:', all(['a', '', 'c']))

# False if all of list items are empty or not zero
print('Any:', any(numbers))
print('Any:', any([1, 0, 2]))
print('Any:', any(['a', 'b', 'c']))
print('Any:', any(['a', '', 'c']))

print('Count:', numbers.count(5))
print('Index:', numbers.index(10))

# in, not in and is, is not operators
print(5 in numbers)
print(99 not in numbers)

list1 = [5, 4, 3]
list2 = [5, 2, 3]
print(list1 == list2)
# first compares 1st items from list if same goes next items to check
print(list1 > list2)

list2 = [5, 4, 3]
print(list1 is list2)  # False - different memory adresses

# Adding Items
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
letters.append('z')
print(letters)

letters = ['a', 'b', 'c']
letters.insert(0, 'x')
letters.insert(3, 'y')
print(letters)

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix.append(['x', 'y', 'z'])
matrix.insert(0, ['a', 'a', 'a'])
print(matrix)

matrix[2].append('x')
matrix[0].insert(0, '*')
print(matrix)

# Removing items
letters = ['a', 'b', 'c']
letters.clear()
print(letters)

letters = ['a', 'b', 'c', 'a']
letters.remove('a')  # removes first match
print(letters)

letters = ['a', 'b', 'c']
print(letters.pop(0))  # returns removed value
removed = letters.pop()  # by default removes last value
print('Removed Item:', removed)

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix.remove(['a', 'b', 'c'])
matrix.pop()

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[1].remove('e')
matrix[0].pop()
matrix[-1].pop(0)
print(matrix)

# Updating items
letters = ['a', 'b', 'c', 'a']
letters[-1] = 'd'
print(letters)

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[-1] = ['x', 'y', 'z']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[-1][-1] = '-'
print(matrix)

# Sorting Lists
letters = ['c', 'a', 'b']
letters.sort()
print(letters)

letters.sort(reverse=True)
print(letters)

matrix = [
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['a', 'b', 'c']
]
matrix.sort()  # sorts by the first item of each inner list
print(matrix)

matrix.sort(reverse=True)
print(matrix)

letters = ['c', 'a', 'b']
new_list = sorted(letters)
print(f'Original List: {letters}')
print(f'Sorted List: {new_list}')

new_list = sorted(letters, reverse=True)
print(f'Original List: {letters}')
print(f'Sorted List: {new_list}')

# Reversing Lists
letters = ['c', 'a', 'b']
letters.reverse()
print(letters)

letters = ['c', 'a', 'b']
new_list = list(reversed(letters))
print(f'Original List: {letters}')
print(f'Reversed List: {new_list}')
