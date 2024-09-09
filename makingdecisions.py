# Determine if user is old enough

age = int(input("How old are you? "))

# Check to see if user is old enough to drive

if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check to see if user is old enough to vote

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote.")

# Check to see if user is old enought to buy alcohol

if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You cannot buy alcohol legally.")

# Check to see if user is old enough for a senior 
# discount

if age >= 65:
    print("You are eligible for the senior discount.")
else: 
    print("You are not eligible for the senior discount.")

