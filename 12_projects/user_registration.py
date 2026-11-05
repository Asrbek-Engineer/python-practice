"""
Secure User Registration System

A simple user registration module that demonstrates:
- Validation functions
- Exception handling (raise / try / except)
- Duplicate checking
- Basic in-memory storage
"""

# ==============================================================
# Part 1: Simulate a Database
# ==============================================================
registered_users = []        # successfully registered users
failed_registrations = []    # failed registration attempts (email + error)


# ==============================================================
# Part 2: Validation Functions
# ==============================================================
def validate_name(name: str) -> bool:
    """
    Check that the name has at least 3 characters (edge spaces are ignored).

    Args:
        name (str): The user's name.

    Returns:
        bool: True if valid, otherwise False.
    """
    return len(name.strip()) >= 3


def validate_email(email: str) -> bool:
    """
    Check that the email contains both '@' and '.'.

    Args:
        email (str): The user's email address.

    Returns:
        bool: True if valid, otherwise False.
    """
    return "@" in email and "." in email


def validate_password(password: str) -> bool:
    """
    Check the password strength.

    Rules:
        - At least 8 characters long
        - At least one uppercase letter
        - At least one digit

    Args:
        password (str): The user's password.

    Returns:
        bool: True if valid, otherwise False.
    """
    return (
        len(password) >= 8
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
    )


# ==============================================================
# Part 3: Main Validation Function (orchestrator)
# ==============================================================
def validate_user_data(name: str, email: str, password: str) -> bool:
    """
    Run all validation functions.

    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        bool: True if all validations pass.

    Raises:
        ValueError: If any validation rule fails (with a clear message).
    """
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


# ==============================================================
# Part 4: Registration Function
# ==============================================================
def create_user_account(name: str, email: str, password: str) -> dict | None:
    """
    Validate the input, check for a duplicate email and register the user.

    Args:
        name (str): The user's name.
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        dict: The created user if registration succeeds.
        None: If validation or the duplicate check fails
              (the error is stored in failed_registrations).
    """
    try:
        validate_user_data(name, email, password)

        is_email_duplicate = any(
            user["email"] == email for user in registered_users
        )
        if is_email_duplicate:
            raise ValueError(f"User with email {email} already exists")

        user_data_container = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active",
        }
        registered_users.append(user_data_container)
        return user_data_container

    except ValueError as e:
        failed_registrations.append({"email": email, "error": str(e)})
        return None


# ==============================================================
# Tests
# ==============================================================
def run_tests() -> None:
    """Run sample registration scenarios and print the results."""
    test_cases = [
        ("Asrbek", "asrbek@mail.com", "Secret123"),    # valid
        ("Ali", "asrbek@mail.com", "Secret123"),       # duplicate email
        ("Al", "al@mail.com", "Secret123"),            # name too short
        ("Maria", "maria.mail.com", "Secret123"),      # no '@'
        ("Sarah", "sarah@mail.com", "weakpass"),       # weak password
    ]

    for index, (name, email, password) in enumerate(test_cases, start=1):
        result = create_user_account(name, email, password)
        status = "OK" if result else "FAILED"
        print(f"Test {index}: {status} -> {email}")

    print(f"\nRegistered: {len(registered_users)}")   # expected: 1
    for user in registered_users:
        print(f"  {user['name']} <{user['email']}>")

    print(f"\nFailed: {len(failed_registrations)}")   # expected: 4
    for failure in failed_registrations:
        print(f"  {failure['email']}: {failure['error']}")


if __name__ == "__main__":
    run_tests()
