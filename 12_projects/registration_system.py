"""
    Secure User Registration System
"""
# Part 1: Simulate a Database
registered_users = list()  # store successfully registered users
failed_registrations = list()  # store information about failed registration attempts

# Part 2: Validation Functions
def validate_name(name):
    return len(name.strip()) >= 3

def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    return (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
    )

# Part 3: Main Validation Function
def validate_user_data(name, email, password):
    if not validate_name(name):
        raise ValueError("Invalid name: must contain at least 3 characters")
    if not validate_email(email):
        raise ValueError("Invalid email: must contain '@' and '.'")
    if not validate_password(password):
        raise ValueError(
            "Invalid password: must be at least 8 characters long "
            "and contain at least one uppercase letter and one digit"
        )
    return True

# Part 4: Registration Function
def create_user_account(name, email, password):
    try:
        validate_user_data(name, email, password)
        is_email_duplicate = any(
            user["email"] == email for user in registered_users)
        if is_email_duplicate:
            raise ValueError(
                f"User with email {email} already exists"
            )
        user_data_container = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active"
        }
        registered_users.append(user_data_container)
        return user_data_container
    except ValueError as e:
        failed_registrations.append({"email": email, "error": str(e)})
        return None

create_user_account("Asrbek", "a@mail.com", "Secret123")
create_user_account("Ali", "a@mail.com", "Secret123")
create_user_account("Al", "b@mail.com", "Secret123")
print(len(registered_users), len(failed_registrations))

print(registered_users, failed_registrations)
