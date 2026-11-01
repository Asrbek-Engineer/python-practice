# While Loops
count = 1
while count <= 5:
    print(count)
    count += 1

while input("Do You Agree? (yes/no): ") != "yes":
    pass
print("Thank You!")

# while True:
#    print("I'm unstoppable!!!") # to stop shortcut: ctrl + c

while True:
    if input("Do You Agree? (yes/no): ") == "yes":
        break
print("Thank You!")

# Challenge
# 1: Allow up to 3 attempts
# 2: If the user types "yes", print "Glad we are on the same page"
# 3: Otherwise, print "3 Strikes, You are Out!"
attempt = 0
while True:
    attempt += 1
    if input("Do You Agree? (yes/no): ").strip().lower() == "yes":
        print("Glad we are on the same page")
        break
    elif attempt == 3:
        print("3 Strikes, You are Out!")
        break

# Better
attempt = 0
while attempt < 3:
    if input("Do You Agree? (yes/no): ").strip().lower() == "yes":
        print("Glad we are on the same page")
        break
    attempt += 1
else:
    print("3 Strikes, You are Out!")
