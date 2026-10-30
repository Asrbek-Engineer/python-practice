import math
import random
from decimal import Decimal, ROUND_HALF_UP

# NOTE: do not name this file numbers.py, math.py, random.py ...
# A file with the same name as a standard module hides it and breaks imports.

# ==============================================================
# Number Types
# ==============================================================
x = 5        # int
y = 5.7      # float
z = 2 + 3j   # complex (rarely used in data engineering)

print(type(x))
print(type(y))
print(type(z))

# Convert types
x = int("24")      # str -> int
print(type(x))

x = 3.14
print(int(x))      # 3: int() drops the decimal part

x = 3
y = 4
print(complex(x, y))   # (3+4j)

# ==============================================================
# Number Operators
# ==============================================================
print(2 + 3)    # 5
print(5 - 2)    # 3
print(4 * 2)    # 8
print(7 / 2)    # 3.5: "/" always returns a float
print(7 // 2)   # 3: floor division
print(7 % 2)    # 1: remainder (modulo)
print(2 ** 5)   # 32: power, 2*2*2*2*2

x = 2
x += 3          # same as x = x + 3
print(x)        # 5

# Measure distance
print(abs(2 - 10))   # 8

# ==============================================================
# Rounding Numbers
# ==============================================================
price = 55.75677623
print(round(price))        # 56
print(round(price, 2))     # 55.76

print(math.floor(price))   # 55: always down
print(math.ceil(price))    # 56: always up
print(math.trunc(price))   # 55: cuts the decimal part
print(int(price))          # 55: same as trunc, no import needed

# ==============================================================
# Random
# ==============================================================
print(random.random())        # float between 0.0 and 1.0
print(random.randint(1, 6))   # int between 1 and 6 (both included)

# ==============================================================
# Validation
# ==============================================================
x = 7.0
print(x.is_integer())      # True: 7.0 has no decimal part

y = 7.1
print(y.is_integer())      # False

# False: 7.0 is a float, even if it looks like an integer
print(isinstance(x, int))
print(isinstance(y, int))  # False

# ==============================================================
# Traps (from the quiz)
# ==============================================================
# 1. Floor division goes DOWN (towards minus infinity), not towards zero
print(-7 // 2)                              # -4 (not -3)

# 2. floor goes down, trunc just cuts the decimal part
#    -> same result for positive numbers, different for negative numbers
print(math.floor(-3.5), math.trunc(-3.5))   # -4 -3

# 3. round() uses "round half to even" (banker's rounding):
#    only when the value is exactly .5, it goes to the nearest EVEN number
print(round(2.5), round(3.5))               # 2 4
print(round(2.6))                           # 3: not a tie, normal rounding

# 4. Floats are stored in binary, so most decimals are not exact
print(0.1 + 0.2)                            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)                     # False

# 5. Compare floats with math.isclose(): True if the difference is tiny
#    (default: relative difference smaller than 0.000000001)
print(math.isclose(0.1 + 0.2, 0.3))         # True

# Bonus: 2.675 is stored as 2.67499999..., so it rounds down
print(round(2.675, 2))                      # 2.67

# ==============================================================
# Challenges
# ==============================================================
# Challenge 1: even or odd
random_integer = random.randint(1, 100)
is_even = random_integer % 2 == 0
print(f"Number: {random_integer}, is even: {is_even}")

# Challenge 2: receipt
# Money -> use Decimal (exact), not float, and create it from a STRING
#   Decimal("0.1") -> exactly 0.1
#   Decimal(0.1)   -> 0.1000000000000000055511151231257827... (float error copied)
price = Decimal("$1,299.90".strip("$").replace(",", ""))
quantity = int("3")
discount = Decimal("15%".replace("%", "")) / 100

cent = Decimal("0.01")   # quantize(cent) -> round to 2 decimal places
subtotal = price * quantity
discount_amount = (subtotal * discount).quantize(cent, rounding=ROUND_HALF_UP)
total = subtotal - discount_amount

print(f"Subtotal: {subtotal:>10,.2f}")          # 3,899.70
print(f"Discount: {discount_amount:>10,.2f}")  # 584.96
# 3,314.74 (subtotal - discount matches)
print(f"Total:    {total:>10,.2f}")

# Challenge 3: pipeline duration
duration_ms = 7384512
total_seconds = duration_ms // 1000
hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60
milliseconds = duration_ms % 1000
# 2h 03m 04s 512ms
print(f"{hours}h {minutes:02d}m {seconds:02d}s {milliseconds}ms")
