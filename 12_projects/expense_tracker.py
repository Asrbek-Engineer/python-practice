"""
Expense Tracker

A simple in-memory expense tracker that demonstrates:
- Input validation and type conversion
- Exception handling (raise / try / except)
- Aggregation with loops (total, total by category)
"""

# ==============================================================
# Part 1: Simulate a Database
# ==============================================================
expenses = []  # store all expense entries


# ==============================================================
# Part 2: Expense Function
# ==============================================================
def add_expense(amount: float | str, category: str, description: str) -> dict | None:
    """
    Validate the amount and add a new expense.

    Rules:
        - The amount must be a number (text like "12.99" is converted)
        - The amount must be greater than zero

    Args:
        amount (float | str): The expense amount.
        category (str): The expense category (edge spaces are removed).
        description (str): A short description of the expense.

    Returns:
        dict: The created expense if it is valid.
        None: If the amount is invalid (the reason is printed).
    """
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError(f"Amount is Zero or Below: {amount}")
        expense_container = {
            "amount": amount,
            "category": category.strip(),
            "description": description,
        }
        expenses.append(expense_container)
        return expense_container
    except (ValueError, TypeError) as e:
        print(str(e))
        return None


# ==============================================================
# Part 3: Total Expenses
# ==============================================================
def calculate_total_expenses() -> float:
    """
    Calculate the sum of all expenses.

    Returns:
        float: The total amount of all expenses (0 if there are none).
    """
    total_expense = 0
    for item in expenses:
        total_expense += item["amount"]
    return total_expense


# ==============================================================
# Part 4: Total by Category
# ==============================================================
def calculate_total_by_category(category: str) -> float:
    """
    Calculate the sum of expenses for one category.

    The comparison ignores edge spaces and upper/lower case.

    Args:
        category (str): The category to sum, e.g. "Food".

    Returns:
        float: The total for the category (0 if not found).
    """
    total_category_expense = 0
    for item in expenses:
        if category.strip().lower() == item["category"].lower():
            total_category_expense += item["amount"]
    return total_category_expense


# ==============================================================
# Part 5: All Expenses
# ==============================================================
def show_expenses() -> None:
    """Print every stored expense, one per line."""
    for item in expenses:
        print(f"{item}")


# ==============================================================
# Tests
# ==============================================================
def check(label: str, actual, expected) -> None:
    """Print PASS if actual equals expected, otherwise FAIL."""
    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] {label}: got {actual!r}, expected {expected!r}")


def run_tests() -> None:
    """Run sample scenarios for every function."""
    print("--- add_expense ---")
    result = add_expense(50, "Food", "Lunch")
    check("valid expense returns a value (not None)", result is not None, True)
    check("returns the new entry (dict)", isinstance(result, dict), True)
    add_expense(120, " Transport ", "Taxi")
    add_expense(30, "Food", "Coffee")
    check("zero amount rejected", add_expense(0, "Food", "Free"), None)
    check("negative amount rejected", add_expense(-10, "Food", "Refund"), None)
    check("non-number amount rejected", add_expense("abc", "Food", "Bad"), None)
    check("3 valid entries stored", len(expenses), 3)
    check("category spaces stripped", expenses[1]["category"], "Transport")

    print("\n--- totals ---")
    check("total of all expenses", calculate_total_expenses(), 200)
    check("total for Food", calculate_total_by_category("Food"), 80)
    check("total for ' Transport ' (with spaces)",
          calculate_total_by_category(" Transport "), 120)
    check("total for 'food' (lowercase)",
          calculate_total_by_category("food"), 80)
    check("total for unknown category", calculate_total_by_category("Rent"), 0)

    print("\n--- edge cases ---")
    check("text amount '50' converted", add_expense(
        "50", "Food", "Text")["amount"], 50.0)
    check("decimal amount kept", add_expense(
        12.99, "Food", "Snack")["amount"], 12.99)
    check("small positive amount accepted", add_expense(
        0.5, "Food", "Gum") is not None, True)

    print("\n--- show_expenses ---")
    show_expenses()


if __name__ == "__main__":
    run_tests()
