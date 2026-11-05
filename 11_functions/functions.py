from pathlib import Path
import math
# Functions
def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")
print("Wake up")
make_coffee()
print("Learning for a while")
make_coffee()

# Built-in Function (Just Calling)
print(len("Python"))

# Function From Libraries (Import Then Call)
number = 4.2
print(math.ceil(number))

# User Defined Function (Define Then Call)
def greet():
    print("Hello")
greet()

def clean_name(name):
    print(name.strip().lower())
clean_name(" MariA  ")
clean_name("KUMAR ")

case_rule = "lower"  # global variable
def clean_name(name):  # parameter
    cleaned = name.strip()  # local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)

clean_name(" MariA  ")
print("The Rule is:", case_rule)

# Building full Clean Name
def clean_full_name(first_name, last_name, country):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)

# Positional Arguments
clean_full_name(" MariA  ", "SMITH ", "USA")

# Keyword Arguments
clean_full_name(first_name=" MariA  ", last_name="SMITH ", country="USA")

# Mixed Arguments
# Rule: Start with Postional Arguments then Keyword
clean_full_name(" MariA  ", last_name="SMITH ", country="USA")

# Default
def clean_full_name(first_name="n/a", last_name="n/a", country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)
clean_full_name("Kumar")

# calc the total of values
def total(*args):
    print(sum(args))

total(1, 2, 3)
total(1, 23, 3, 34, 5, 90, 111)

# create the user profile
def create_user(**kwargs):
    print(type(kwargs))  # Dictionary type
    print(kwargs)

create_user(
    first_name="Linus",
    last_name="Torvalds",
    age=56,
    country="Finland"
)

# Return
def clean_name(name):
    cleaned = name.strip().lower()
    return cleaned  # if has no return than by default returns None
cln_name = clean_name(" MariA  ")
print(cln_name)

def clean_name(name):
    if not name.strip():
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned
cln_name = clean_name("")
print(cln_name)

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned
lo_name, up_name = clean_name(" MariA  ")
print(lo_name)
print(up_name)

# Action Function
# Task: store application log messages in a file
def write_log(message):
    with open(r"C:\Users\Acer\projects\python-practice\11_functions\app.log", "a") as file:  # "a" means append
        file.write(message + "\n")
write_log("App Started")

# my extend
# read from file
def read_log():
    with open(r"C:\Users\Acer\projects\python-practice\11_functions\app.log", "r") as file:  # "r" means read
        content = file.read()
        print(content)
read_log()

# Define file path
file_path = Path(
    r"C:\Users\Acer\projects\python-practice\11_functions\app.log")

# 1 - check if the file actually exists before doing anything
if file_path.exists():
    print(f"File found! Size: {file_path.stat().st_size} bytes")

# 2 - rename or move file
# new_path = Path(r"C:\Users\Acer\projects\python-practice\11_functions\old_app.log")
# file_path.rename(new_path)

# 3 - delete file
# file_path.unlink()

# Transformation Function
# Task: clean an email and split it into username and domain
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split("@")
    return {"username": username, "domain": domain}

print(clean_and_split_email(" SARA@gmAIl.com "))

# Validation Function
# Task: check if a password meets the minimum length of 8
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("123456"))
print(is_valid_password("12345678"))

# Task: check if email has a basic valid format
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("saragmail.com"))
print(is_valid_email("sara@gmailcom"))
print(is_valid_email("sara@gmail.com"))


# Orchestrator Function
def process_user_email(email):
    write_log("App Started")
    # we must check if it is valid
    # if it is not valid, we log the problem
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    # if it is valid we clean it and store structured information
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {email}")
    write_log("App Stopped")

# we receive an email from a user
email = input("Please enter Your Email:")
process_user_email(email)

print("=====LOG=====")
read_log()
print("=============")

# Writing Clean Function
def calculate_discount(price: float, rate: float) -> float:
    """
        Calculating the final price after applying a discount.
        Args:
            price (float): Original price before discount
            rate (float): Discount Rate as number (e.g 20 for 20%)
        Returns:
            final_price (float): Final Price after applying discount.
    """
    final_price = price - (price * rate / 100)
    return final_price

help(calculate_discount)
print("Calculating Discount")
print(calculate_discount(80, 20))
