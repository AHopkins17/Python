# Ask user to input two distinct integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Logical comparisons for operator 'and'

print(f"Both numbers greater than 4: {num1 > 4 and num2 > 4}")
print(f"Both numbers less than 100: {num1 < 100 and num2 < 100}")

# Logical comparisons for operator 'or'

print(f"Either number is greater than 15: {num1 > 15 and num2 > 15} ")
print(f"Either number is odd: {num1 % 2 != 0 or num2 % 2 != 0}")

# Logical comparisons for operator 'not'

print(f"num1 is not equal to num2: {not (num1 == num2)}")
print(f"num2 is not less than 0: {not (num2 < 0)}")