# Determine the letter grade from the numeric grade.

grade = int(input("Enter the numeric grade: "))

if grade >= 90 and grade <= 100:
    print("The letter grade is: A")
elif grade >= 80 and grade <= 89:
    print("The letter grade is: B")
elif grade >= 70 and grade <= 79:
    print("The letter grade is: C")
elif grade >= 60 and grade <= 69:
    print("The letter grade is: D")
elif grade <= 59:
    print("The letter grade is: F")
else:
    print("Please enter valid numeric grade between 0 and 100.") 
