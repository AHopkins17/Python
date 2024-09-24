# calculate_interest

def calculated_interest(principal, rate, time):
    # Calculation
    interest = (principal * rate * time) / 100
    return interest

#  Get user input
principal_amount = int(input("Enter the principal amount: "))
interest_rate = int(input("Enter the interest rate as a whole number (5% would be 5): "))
investment_time = int(input("Enter the investment time in whole years: "))

# Call the function and store results
calculated_interest = calculated_interest(principal_amount, interest_rate, investment_time)

#Print the result in user-friendly format
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${calculated_interest:,.2f}")