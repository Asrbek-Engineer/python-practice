# Lists
my_list = [10, 30, 20, 10]
print(my_list)  # Ordered # Allow Duplicates
print(my_list[1])  # Indexed
my_list[3] = 40  # Mutable
print(my_list)

# Tuples
my_tuple = (10, 30, 20, 10)
print(my_tuple)  # Ordered # Allow Duplicates
print(my_tuple[1])  # Indexed
# my_tuple[3] = 40 # print(my_tuple) # Immutable

# Sets
my_set = {10, 30, 20, 10}
print(my_set)  # Unordered # Unique
# print(my_set[1]) # Not Indexed
my_set.remove(20)  # Mutable
print(my_set)


# Set Methods
a = {10, 20, 30, 40}
a.add(50)
# a.update({1, 2})
a |= {1, 2}  # same as update method
print(a)

a.remove(2)  # removes valid value otherwise returns KeyError
a.discard(100)  # removes value if it don't exists returns nothing
print(a)


a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
# Mathematical Operations
print(a.union(b))
print(a | b)  # same as union method

print(a.intersection(b))
print(a & b)  # same as intersection method

print(a.difference(b))
print(a - b)  # same as difference method

print(a.symmetric_difference(b))
print((a - b) | (b - a))
print(a ^ b)  # same as symmetric_difference method


a = {10, 20}
b = {10, 20, 50, 60}
# Set Relationships
print(a.issubset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))


# Dictionaries
my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 50,
}
print(my_dict)  # Ordered, Keys are Unique, Values Allow Duplicates
# print(my_dict[1])  # Not Indexed
print(my_dict['a'])  # Call Value with Key
my_dict['c'] = 80  # Mutable
print(my_dict)

# Dictionary Methods
user = {"id": 1, "age": 30, "city": "berlin"}
# Access
print(user["age"])
# By default returns None if missing but we can change returning value
print(user.get("name", "Unknown"))

# Check
print("age" in user)
print("name" not in user)

# View Objects
print(user.keys())
print(user.values())
# shows (key, value) like tuple perfect for looping, transforming or building new dict
print(user.items())

# Looping
for key, value in user.items():
    print(key, value)

# Add, Remove, Update
user["name"] = "John"  # Add
user["age"] = 35  # Update
user.update({"age": 40, "city": "Paris"})
print(user)

age = user.pop("age", "Not Found")
print("Removed item:", age)

user.popitem()  # Removes last item
print(user)

# Creation
user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)

user["age"] = 30
print(user)

# 1 - Use Case: Representing a Single Row from a Database or API
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}

# 2 - Use Case: Mapping Translations to Friendly Values
status_map = {
    "01": "Open",
    "02": "In Progress",
    "03": "Done"
}

# 3 - Use Case: Turning short abbreviations into full readable names
country_map = {
    "DE": "Germany",
    "FR": "France",
    "IN": "India"
}

# 4 - Use Case: Storing Environment Variables & Configuration
system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DP_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytics_warehouse"
}

# 5 - Use Case: ETL and Pipeline Settings
etl_config = {
    "DEBUG_MODE": False,                        # Turn verbose logging on/off
    "BATCH_SIZE": 500,                          # How many rows to process per batch
    "LOG_LEVEL": "INFO",                        # Logging verbosity
    "SOURCE_PATH": "/data/bronze/",             # Where raw files live
    "TARGET_PATH": "/data/silver/",             # Where cleaned files go
    "RETRY_COUNT": 3,                           # How many times to retry a failed extr
    "FAIL_ON_ERROR": False,                     # Keep going or stop the job
    "VALIDATE_SCHEMA": True,                    # Enforce schema check
    "SUPPORTED_FORMATS": ["csv", "parquet"],    # Allowed file
    "RUN_ENV": "production"                     # dev / test / prod
}

# 6 - Use Case: Metadata
table_metadata = {
    "table_name": "customers",
    "columns": {
        "id": {"type": "integer", "nullable": False},
        "name": {"type": "string", "nullable": True},
        "age": {"type": "integer", "nullable": True},
        "country": {"type": "string", "nullable": True}
    },
    "row_count": 105320,
    "file_format": "parquet",
    "last_updated": "2024-10-01T12:45:00Z",
    "partition_by": ["country"],
    "tags": ["pii", "customer-data"],
}

# Dictionary Challenge: Keep Only String Values & Convert Them to UPPERCASE
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}
upper_user_string = {
    key: value.upper()  # Expression
    for key, value in user.items()  # Loop
    if isinstance(value, str)  # Filter
}
print(upper_user_string)
