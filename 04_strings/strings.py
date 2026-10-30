# Types
name = 'Asrbek'
print(type(name))

age = 25
print(type(age))  # integer
# print("Your age is:" + age) # type error
print("Your age is:" + str(age))
age = str(age)
print(type(age))  # string

# Math
password = "123abc456"
print(len(password))

if len(password) < 8:
    print("Your Password is too short!")

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

print(text.count("Python"))  # case-sensitive returns 2
# Use case - Detect Quality Issues
print(text.count("$"))

# Transformations
# Replace
phone_number = "123-45-67"
print(phone_number.replace("-", "/"))
print(phone_number.replace("-", ""))

price = "1234,56"
print(price.replace(",", "."))

price = "$1299,99"
print(price.replace("$", "").replace(",", "."))

# Replace Challenge
# Convert the messy phone number into a clean number format with only digits -> 00491761234567
phone_number = "+49 (176) 123-4567"
phone_number = phone_number.replace("(", "").replace(")", "").replace(
    "+", "00").replace("-", "").replace(" ", "")
print(phone_number)

first_name = "Michael"
last_name = "Scott"
full_name = first_name + " " + last_name
print(full_name)

folder = "C:/Users/Acer/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

# fstring
name = "Sam"
age = 25
is_student = False
print(
    f"My name is {name}, I am {age} years old and student status is {is_student}.")
print(f"2 + 3 = {2 + 3}")
print(f"{{This is me}}")  # print with curly braces

# split
stamp = "2026-10-29 19:41"
print(stamp.split(" "))

csv_file = "1234,Max,USA,1970-01-01,M"
print(csv_file.split(","))

# Repetition
print("ha" * 3)
print("=" * 30)

# Indexing and Slicing
text = "Python"

# first character
print(text[0])
print(text[-6])

# last character
print(text[5])
print(text[-1])

# extract year
date = "2026-10-29"
print(date[0:4])
print(date[:4])

# extract month
print(date[5:7])

# extract day
print(date[8:])
print(date[-2:])
# Use positive number from left to right
# Use negative number from right to left

# Whitespace Cleanup
text = "  Engineering".lstrip()
print(text)

text = "Engineering  ".rstrip()
print(text)

text = "  Engineering  ".strip()
print(text)

text = "###abc###".strip("#")
print(text)

text = "  Engineering"
nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of Spaces:", nr_of_spaces)
print("Is My Data Clean?", is_clean)

# Case Conversions
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

# Best Practice - Clean Before Search
search = "Email".lower().strip()
data = " emAiL   ".lower().strip()

print(search == data)

# Search
phone = "+99800-123-4567"
print("Is Uzbekistan phone code?", phone.startswith("+998"))

file = "data_backup.csv"
print("Is CSV File?", file.endswith(".csv"))

email = "engineer@gmail.com"
print("Is Gmail?", email.endswith("gmail.com"))

print("Is Email?", "@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)


phone1 = "+99800-123-4567"
phone2 = "99800-321-4567"
phone3 = "998-456-4567"

print(phone1[phone1.find("-") + 1:])
print(phone2[phone2.find("-") + 1:])
print(phone3[phone3.find("-") + 1:])

# Validation
country = "USA"
print("Is Alphabetic?", country.isalpha())

phone = "00123456789"
print("Is Numeric?", phone.isdigit())
print("Is Numeric?", phone.isnumeric())

# Challenge
# Turn the messy string into a single clean summary with name, role and age
# "968-Maria, ( D@t@ Engineer );; 27y  "
messy_info = "968-Maria, ( D@t@ Engineer );; 27y  "
name = messy_info[messy_info.find("-") + 1:messy_info.find(",")].lower()
role = messy_info[messy_info.find(
    "(") + 1:messy_info.find(")")].strip().replace("@", "a").lower()
age = messy_info[messy_info.find(";") + 2:].strip().strip("y")
clean_info = f"name: {name} | role: {role} | age: {age}"
print(clean_info)
