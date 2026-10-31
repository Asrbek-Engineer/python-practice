# ==============================================================
# CONDITIONAL STATEMENTS
# ==============================================================

# --if--
# Runs the block only when the condition is True
# The block is defined by indentation (4 spaces), not by brackets
age = 20
if age >= 18:
    print("Adult")

# --if / else--
# else runs when the condition is False
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# --if / elif / else--
# Checks conditions from top to bottom and runs ONLY the first True one
# -> the ORDER matters: put the most specific (narrow) condition first
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"   # 85 stops here, the next elif is not checked
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)      # B

# Wrong order -> wrong result
if score >= 70:
    grade = "C"   # 85 >= 70 is True, so it stops here
elif score >= 80:
    grade = "B"   # never reached for 85
print(grade)      # C (wrong!)

# --Nested if--
# An if inside another if; keep it to 2 levels max, otherwise it gets hard to read
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin:
        print("Admin panel")
    else:
        print("User dashboard")

# Often a flat version with "and" is cleaner
if is_logged_in and is_admin:
    print("Admin panel")

# --Truthy / Falsy values in conditions--
# Falsy: False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict)
# Everything else is Truthy
name = ""
if not name:
    print("Name is empty")        # same as: if name == ""

items = []
if not items:
    print("No items")             # same as: if len(items) == 0

# Do not write: if is_admin == True:   -> just write: if is_admin:

# --Guard clause: check invalid values FIRST--
# Invalid input is handled at the top, so it cannot slip into a normal branch
aqi = -5
if aqi < 0:
    print("Invalid AQI")
elif aqi <= 50:
    print("Good")

# --Ternary (one-line if / else)--
# value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)                     # adult

# Useful for small choices; for complex logic use a normal if / elif
price = 120
shipping = 0 if price >= 100 else 10
print(f"Shipping: {shipping}")    # Shipping: 0

# --match-case (Python 3.10+)--
# Compares one value with several patterns, like CASE WHEN in SQL
gender_code = " f "
match gender_code.strip().upper():
    case "F":
        gender = "Female"
    case "M":
        gender = "Male"
    case _:                       # "_" = everything else, like ELSE in SQL
        gender = "n/a"
print(gender)                     # Female

# Several values in one case with "|"
status_code = 404
match status_code:
    case 200 | 201:
        print("Success")
    case 400 | 404:
        print("Client error")
    case 500:
        print("Server error")
    case _:
        print("Unknown")

# Guard: an extra condition inside a case with "if"
temperature = 35
match temperature:
    case t if t < 0:
        print("Freezing")
    case t if t < 30:
        print("Normal")
    case _:
        print("Hot")              # Hot

# --Walrus operator := (Python 3.8+)--
# Saves a value into a variable AND uses it in the condition at the same time
password = "abc123"
if (length := len(password)) < 8:
    print(f"Too short: {length} characters")   # len() is called only once

# --Common traps--
# 1. "=" assigns, "==" compares:    if x = 5  -> SyntaxError
# 2. Order of elif matters: the first True branch wins
# 3. Wrong indentation changes the logic (or raises IndentationError)
# 4. Do not compare floats with ==, use math.isclose()
# 5. Check None with "is":          if value is None

# ==============================================================
# Challenges
# ==============================================================

# 1 - AQI category + one-line advice
aqi = 187
aqi_type = ""

if aqi < 0:
    aqi_type = "Invalid AQI"
elif aqi <= 50:
    aqi_type = "Good"
elif aqi <= 100:
    aqi_type = "Moderate"
elif aqi <= 150:
    aqi_type = "Unhealthy for Sensitive Groups"
elif aqi <= 200:
    aqi_type = "Unhealthy"
elif aqi <= 300:
    aqi_type = "Very Unhealthy"
else:
    aqi_type = "Hazardous"

advice = "Wear a mask" if aqi > 150 else "No mask needed"
print(f"AQI {aqi}: {aqi_type} | {advice}")

# 2 - Clean a country code with match-case
country = "USA"

code = country.strip().upper()
match code:
    case "DE":
        country = "Germany"
    case "USA" | "US":
        country = "United States"
    case "":
        country = "n/a"
    case _:
        country = code
print(country)

# 3 - Validate emails until a valid one is entered (empty input stops the loop)
while (email := input("Enter Email: ")):
    if (len_email := len(email)) < 6:
        print(f"Too short: {len_email} characters")
    elif "@" not in email:
        print("Missing @")
    elif not email.endswith((".com", ".uz")):
        print("Invalid domain")
    else:
        print("Valid")
        break
