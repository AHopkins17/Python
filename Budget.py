# Description: Budget Breakdown Calculator

# Ask user for total budget
total_budget = float(input("Enter your total budget: $"))

# Ask user for each category amount
print("\nEnter the amount in each category:")

housing = float(input("Housing: $"))
utilities = float(input("Utilities: $"))
groceries = float(input("Groceries: $"))
transportation = float(input("Transportation: $"))
health_care = float(input("Health Care: $"))
personal_care = float(input("Personal Care: $"))
clothing = float(input("Clothing: $"))
debt = float(input("Debt: $"))

# Calculate total spending
total_spent = (housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt)

# Calculate and show each category percentage of total budget
print("Budget Breakdown")

categories = {
    "Housing": housing,
    "Utilities": utilities,
    "Groceries": groceries,
    "Transportation": transportation,
    "Health Care": health_care,
    "Personal Care": personal_care,
    "Clothing": clothing,
    "Debt": debt
}

for category, amount in categories.items():
    percentage = (amount / total_budget) * 100
    print(f"{category:<20} ${amount:<12.2f} {percentage:13.2f}%")
