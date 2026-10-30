# Data Types
a = 3  # int
b = 3.14  # float
c = "Hello"  # str
d = 'Hi'  # str
e = '12345'  # str
f = True  # bool
g = False  # bool
h = None  # NoneType
i = ""  # str - empty string
j = " "  # str - whitespace

text = "hi"
number = 10
print(type(text))
print(type(number))

print(len(text))
# print(len(number)) # type error

print(text.upper())
# print(number.upper()) # attribute error

print(number.bit_length())

age = 26
height = 1.78
name = "Asrbek"
student = False
car = None

print(name, "is", age, "years old", "and with", height, "metres height")
print("Is", name, "student?", student)
print("Does", name, "have a car?", car)
