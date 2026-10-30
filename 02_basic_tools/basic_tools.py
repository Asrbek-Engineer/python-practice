# This is a single-line comment

# This is multi-line comment
# 1. Create User Name
# 2. Print Message to User
# 3. Store Data


# Store the final exam score
x = 10

x = 9  # Final exam score


# PRINT
print("Hello Python")
print('Hello Python')
# print("Hello Python') # syntax error

print("--------------------")
print("    LEARN PYTHON    ")
print("--------------------")

# --Escape sequences--
# Escape Backslash \
print("Hello \"Python\"")
print('Hello \'Python\'')

# Escape Double Backslash \\
print("Path: C:\\Users\\Acer")

# Escape New line \n
print("Message_1\n")
print("Message_2")

print("Message_1\nMessage_2")

# Escape Tab \t
print("Message_1\tMessage_2")

# \n and \\
print("  /\\_/\\\n ( o.o )\n  > ^ <")

# Python Challenge
print("My Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI".expandtabs(4))

# Triple quote
print("""My Learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI""".expandtabs(4))

# --VARIABLES--
name = "Asrbek"
language = "Python"
print("My name is", name)
print(name, "is learning", language)
print(name, "wants to become", language, "Expert")

# Medallion Architecture
dwh = r"""
   ___________
  /           \
 |\___________/|
 |   BRONZE    |
 |\___________/|
 |   SILVER    |
 |\___________/|
 |    GOLD     |
  \___________/
"""
print(dwh)

# --INPUT--
name = input("Enter Your Name:")
country = input("Enter Your Country:")
print(name, "comes from", country)

# Python Challenge
email = input("Enter Email:")
support_email = input("Enter Support Email:")
website = input("Enter website:")

print(email, support_email, website, sep="\n")
