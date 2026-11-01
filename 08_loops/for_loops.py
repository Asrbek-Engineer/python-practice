# ==============================================================
# FOR LOOPS
# ==============================================================

# --Loop over a tuple--
items = (1, 2, 3, 4, "5")
for item in items:
    print(f"Round: {item}")

# --Loop over a list--
items = [1, 2, 3, 4, "Hello"]
for item in items:
    print(f"Round: {item}")

# --Loop over a string (character by character)--
items = "Python"
for item in items:
    print(f"Round: {item}")

# ==============================================================
# range()
# ==============================================================
# range(stop): 0 ... stop-1 (the stop value is NOT included)
for i in range(10):
    print(f"Round: {i}")          # 0 ... 9

# range(start, stop)
for i in range(1, 11):
    print(f"Round: {i}")          # 1 ... 10

# range(start, stop, step): step is 1 by default
for i in range(1, 11, 2):
    print(f"Round: {i}")          # 1, 3, 5, 7, 9

# ==============================================================
# Use Cases
# ==============================================================
# --Aggregation (summary)--
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)      # 265

# --Data cleanup--
files = ["  Report.csv ", "DATA.csV ", "final.TXT"]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")

# TRAP: "file = ..." changes only the loop variable, NOT the list
# ['  Report.csv ', 'DATA.csV ', 'final.TXT'] (unchanged)
print(files)
# To keep the cleaned values -> append them to a new list (Lists section)

# ==============================================================
# break / continue / pass
# ==============================================================
names = ["Ali", "", "Vali", "John", "Jack"]

# --break: stops the whole loop--
for name in names:
    if name == "":
        print("Empty value detected!")
        break
    print(f"Name = {name}")       # only Ali

# --continue: skips the current round, goes to the next one--
for name in names:
    if name == "":
        print("Empty value detected!")
        continue
    print(f"Name = {name}")       # Ali, Vali, John, Jack

# --pass: does nothing, a placeholder for an empty block--
# (Python does not allow an empty block, so "pass" keeps the code valid)
for name in names:
    if name == "":
        pass                      # TODO: handle empty value
    print(f"Name = {name}")

# Real handling instead of pass
for name in names:
    if name == "":
        name = "unknown"
    print(f"Name = {name}")       # Ali, unknown, Vali, John, Jack

# --Skip weekends in a calendar loop--
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    if day in ["Saturday", "Sunday"]:
        continue
    print(day)

# --Stop processing on suspicious input--
emails = [
    "data@gmail.com",
    "baraa@outlook.de",
    "DROP TABLE USERS;",
    "maria@gmail.com"
]
for email in emails:
    if ";" in email:
        print("SQL Injection: Hacker Attack!")
        break
    print(f"Processing Email: {email}")

# ==============================================================
# for-else
# ==============================================================
# "else" runs only when the loop finished WITHOUT break
items = [1, 3, 4, 7]
for item in items:
    print(item)
else:
    print("End")                  # no break -> else runs

# --for-else + break: search pattern--
numbers = [1, 3, 4, 7]
for number in numbers:
    if number % 2 == 0:
        print("Even Number Found:", number)
        break
else:
    print("All numbers are odd")  # runs only if nothing was found

names = ["Kamara", "Tuba", None, "Mounika"]
for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")

files = ["data.csv", "database.CSV", "textbook.txt", "report.csv"]
for file in files:
    if not file.lower().endswith(".csv"):
        print(f"{file} is not CSV")
        break
else:
    print("All files are CSV")

# ==============================================================
# Nested Loops
# ==============================================================
# The inner loop runs completely for EVERY round of the outer loop
for x in range(10):               # outer loop
    row = "("
    for y in range(10):           # inner loop
        if y != 9:
            row += str(abs(x - y)) + ", "
        else:
            row += str(abs(x - y))
    row += ")"
    print(row)

# --All combinations--
colors = ["red", "green", "blue"]
sizes = ["L", "M", "S"]
for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")   # 3 x 3 = 9 lines

# --Generate file names--
years = [2026, 2027]
months = ["Jan", "Feb"]
days = range(1, 29)
for year in years:
    for month in months:
        for day in days:
            # 2 x 2 x 28 = 112 files
            print(f"report_{year}_{month}_{day}.csv")

# --Generate data quality SQL checks--
tables = ["customers", "orders", "products", "employees"]
columns = ["id", "create_date"]
for table in tables:
    for column in columns:
        print(f"SELECT count(*) FROM {table} WHERE {column} IS NULL;")

# ==============================================================
# Challenges
# ==============================================================
# 1 - Times tables from 1 to 10
for i in range(1, 11):
    print(f"\n===== {i} TIMES TABLE =====\n")
    for j in range(1, 11):
        print(f"\t{i} x {j} = {i * j}".expandtabs(6))

# 2 - Draw a tree with *
stars_height = int(input("Enter Tree's Height: "))
for i in range(1, stars_height + 1):
    print(" " * (stars_height - i) + "*" * (2 * i - 1))

# 3 - Find duplicate files
file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]
for file1 in file_list:
    count = 0
    for file2 in file_list:
        if file1 == file2:
            count += 1
    if count > 1:
        print(f"Duplicate Found: {file1}")
        break
else:
    print("All files are unique")
# Later (Sets section): len(file_list) != len(set(file_list)) does it in one line

# ==============================================================
# Common Traps
# ==============================================================
# 1. range(1, 10) stops at 9: the stop value is NOT included
# 2. Changing the loop variable does not change the list
# 3. "else" after a loop runs when there was NO break (not "if the loop was empty")
# 4. pass does nothing: it is only a placeholder for an empty block
