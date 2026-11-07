"""
Mini Banking System

A simple in-memory banking system that demonstrates:
- Functions with validation logic
- Exception handling (raise / try / except)
- Lists and dictionaries as a simulated database
- Transaction history per account
"""

# ==============================================================
# Part 1: Simulate a Database
# ==============================================================
accounts = []  # store all bank accounts


# ==============================================================
# Part 2: Create Account
# ==============================================================
def create_account(name: str, initial_balance: str | float) -> dict | None:
    """
    Create a new bank account.

    Rules:
        - The account name must be unique
        - The initial balance must be a number and not negative

    Args:
        name (str): The account holder's name.
        initial_balance (str | float): The starting balance.

    Returns:
        dict: The created account (name, balance, transactions).
        None: If validation fails (the reason is printed).
    """
    try:
        if find_account(name) is not None:
            raise ValueError(
                f"There is already {name} in accounts"
            )
        initial_balance = float(initial_balance)
        if initial_balance < 0:
            raise ValueError(
                f"Initial Balance is Invalid: {initial_balance}"
            )

        account_container = {
            "name": name,
            "balance": initial_balance,
            "transactions": []
        }
        accounts.append(account_container)
        return account_container
    except (ValueError, TypeError) as e:
        print(str(e))

def find_account(name: str) -> dict | None:
    """
    Find an account by name.

    Args:
        name (str): The account holder's name.

    Returns:
        dict: The account if it exists.
        None: If no account has this name.
    """
    for account in accounts:
        if name == account["name"]:
            return account
    return None

def account_transaction(name: str, amount: str | float, transaction_type: str) -> float:
    """
    Apply a deposit or withdrawal to an account (shared logic).

    Rules:
        - The account must exist
        - The amount must be a number greater than 0
        - A withdrawal cannot be larger than the current balance

    Args:
        name (str): The account holder's name.
        amount (str | float): The transaction amount.
        transaction_type (str): "Deposit" or "Withdrawal".

    Returns:
        float: The updated balance.

    Raises:
        ValueError: If any rule fails or the transaction type is unknown.
    """
    account = find_account(name)
    if not account:
        raise ValueError(f"Account not found: {name}")

    amount = float(amount)
    if amount <= 0:
        raise ValueError(f"Amount is Zero or Below: {amount}")

    if transaction_type == "Deposit":
        account["balance"] += amount
        account["transactions"].append(
            {"type": "Deposit", "amount": amount})

    elif transaction_type == "Withdrawal":
        if account["balance"] < amount:
            raise ValueError(
                "Funds are insufficient"
            )
        account["balance"] -= amount
        account["transactions"].append(
            {"type": "Withdrawal", "amount": amount})
    else:
        raise ValueError(f"Unknown transaction type: {transaction_type}")
    return account["balance"]

# ==============================================================
# Part 3: Deposit Function
# ==============================================================
def deposit(name: str, amount: str | float) -> float | None:
    """
    Deposit money into an account.

    Args:
        name (str): The account holder's name.
        amount (str | float): The amount to deposit (must be greater than 0).

    Returns:
        float: The updated balance.
        None: If the deposit fails (the reason is printed).
    """
    try:
        return account_transaction(name, amount, "Deposit")
    except (ValueError, TypeError) as e:
        print(str(e))

# ==============================================================
# Part 4: Withdraw Function
# ==============================================================
def withdraw(name: str, amount: str | float) -> float | None:
    """
    Withdraw money from an account.

    Args:
        name (str): The account holder's name.
        amount (str | float): The amount to withdraw (must be greater than 0
            and not larger than the balance).

    Returns:
        float: The updated balance.
        None: If the withdrawal fails (the reason is printed).
    """
    try:
        return account_transaction(name, amount, "Withdrawal")
    except (ValueError, TypeError) as e:
        print(str(e))

# ==============================================================
# Part 5: Show Account Summary
# ==============================================================
def show_account(name: str) -> None:
    """
    Display the account name, current balance and all transactions.

    Args:
        name (str): The account holder's name.
    """
    the_account = find_account(name)
    if the_account is None:
        print(f"Account not found: {name}")
        return

    print(f"Account: {the_account["name"]}")
    print(f"Balance: {the_account["balance"]:,.2f}")
    for i, transaction in enumerate(the_account["transactions"], start=1):
        print(
            f"\t{i} {transaction["type"]:<12} {transaction["amount"]:,.2f}".expandtabs(2))

# ==============================================================
# Part 6: Testing Section
# ==============================================================
def check(label: str, actual, expected) -> None:
    """Print PASS if actual equals expected, otherwise FAIL."""
    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] {label}: got {actual!r}, expected {expected!r}")


def attempt(func, *args):
    """
    Call a banking function and report what happened.

    Works whether the function raises ValueError or catches it and returns None.

    Returns:
        tuple: ("ok", result) on success, ("rejected", reason) on failure.
    """
    try:
        result = func(*args)
    except ValueError as e:
        return ("rejected", str(e))
    if result is None:
        return ("rejected", "returned None")
    return ("ok", result)


def get_account(name: str) -> dict | None:
    """Find an account in the accounts list by name (test helper)."""
    for account in accounts:
        if account["name"] == name:
            return account
    return None


def count_transactions(name: str, transaction_type: str) -> int:
    """Count transactions of one type for an account (test helper)."""
    account = get_account(name)
    return sum(1 for t in account["transactions"] if t["type"] == transaction_type)


def run_tests() -> None:
    """Run all scenarios required by the project."""
    print("--- create_account ---")
    status, result = attempt(create_account, "Asrbek", 1000)
    check("create account", status, "ok")
    check("returns a dict", isinstance(result, dict), True)
    check("account has name, balance, transactions",
          set(get_account("Asrbek").keys()) >= {"name", "balance", "transactions"}, True)
    check("transactions is a list", isinstance(
        get_account("Asrbek")["transactions"], list), True)
    check("duplicate account rejected", attempt(
        create_account, "Asrbek", 500)[0], "rejected")
    check("negative initial balance rejected", attempt(
        create_account, "Vali", -100)[0], "rejected")
    check("zero initial balance allowed", attempt(
        create_account, "Sara", 0)[0], "ok")
    check("2 accounts stored", len(accounts), 2)

    print("\n--- deposit ---")
    check("deposit 500 returns new balance", attempt(
        deposit, "Asrbek", 500), ("ok", 1500))
    check("deposit 250.5 returns new balance", attempt(
        deposit, "Asrbek", 250.5), ("ok", 1750.5))
    check("deposit 0 rejected", attempt(deposit, "Asrbek", 0)[0], "rejected")
    check("negative deposit rejected", attempt(
        deposit, "Asrbek", -50)[0], "rejected")
    check("deposit to unknown account rejected",
          attempt(deposit, "Ghost", 100)[0], "rejected")
    check("balance after deposits", get_account("Asrbek")["balance"], 1750.5)

    print("\n--- withdraw ---")
    check("withdraw 300 returns new balance", attempt(
        withdraw, "Asrbek", 300), ("ok", 1450.5))
    check("withdraw 450.5 returns new balance", attempt(
        withdraw, "Asrbek", 450.5), ("ok", 1000))
    check("overdraft rejected", attempt(
        withdraw, "Asrbek", 5000)[0], "rejected")
    check("balance unchanged after overdraft",
          get_account("Asrbek")["balance"], 1000)
    check("withdraw 0 rejected", attempt(withdraw, "Asrbek", 0)[0], "rejected")
    check("withdraw from unknown account rejected",
          attempt(withdraw, "Ghost", 10)[0], "rejected")
    check("withdraw from zero balance rejected",
          attempt(withdraw, "Sara", 0.01)[0], "rejected")
    attempt(deposit, "Sara", 100)
    check("withdraw exact balance allowed",
          attempt(withdraw, "Sara", 100), ("ok", 0))

    print("\n--- transactions ---")
    check("2 Deposit transactions", count_transactions("Asrbek", "Deposit"), 2)
    check("2 Withdrawal transactions (overdraft not recorded)",
          count_transactions("Asrbek", "Withdrawal"), 2)

    print("\n--- show_account ---")
    show_account("Asrbek")

if __name__ == "__main__":
    run_tests()
