# Boolean
print(bool(1234))  # True
print(bool("Hi"))  # True
print(bool())  # False
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False

email = ""
phone = "1234-56789"
username = ""
# Allows registration if any field is filled
print(any([email, phone, username]))  # True - at least one of them is True

# Allows registration only if all fields are filled
print(all([email, phone, username]))  # False: all values must be truthy

# Check data type of value
print(isinstance(123, int))
print(isinstance(True, str))

# Comparison operators
print(10 == 10)
print(10 != 10)
print(6 > 3)
print(6 >= 3)
print(3 < 7)
print(7 <= 7)
# compares alphabetically
print("a" < "b")
print("a" == "b")
print("a" == "A")  # False - Case Sensitive

# Chained comparison
print(1 < 5 < 10)
print(1 < -2 < 10)
print(1 < 5 < 0)

# Is age between 18 and 30?
age = 20
print(18 <= age <= 30)

# Logical Operators
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# checks if the system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

# checking user credentials before login
email = True
password = False
print(email and password)

print(not 3 > 1)
print(not False)

name = ""
print(not name)
print(not 0)

# Allow access only if the user is logged in or they are guest but they must not banned
is_logged_in = True
is_guest = not is_logged_in
is_banned = True
print((is_logged_in or is_guest) and not is_banned)

# Membership operators
print("h" in "python")
print(1 not in [1, 2, 3])

# Security check: ensure the domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

# Identity Operators
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
# True only because Python caches small ints (-5..256); compare values with ==
print(x is y)

x = ['a', 'b', 'c']
y = x  # same object/instance
print(x == y)
print(x is y)

# Make sure the email exists and it is not empty
email = None
print(email is not None and email != "")

# Challenges
# 1 - Check if a user's name is not empty and age is greater than or equal to 18
# 2 - Check if the password is at least 8 characters long and does not contain spaces
# 3 - Check if a user's email is not empty, contains '@' and ends with '.com'
# 4 - Check if a username is a string, is not None and is longer than 5 characters
# 5 - Check if the user is either an admin or a moderator and
#     either they're not banned or they've verified their email

# 1
name = "Asrbek"
age = 26
print(name.strip() != "" and age >= 18)

# 2
password = "1234_ asdf "
print(len(password) >= 8 and " " not in password)

# 3
email = "something@gmail.com"
print(email != "" and "@" in email and email.endswith(".com"))

# 4
print(isinstance(name, str) and len(name) > 5)

# 5
is_admin = True
is_moderator = True
is_banned = False
is_email_verified = True
print((is_admin or is_moderator) and (not is_banned or is_email_verified))
