# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime, timedelta

def main():
    print("\n\n")    # Space for neatness

    try:
        # Get today's date
        today = datetime.today()

        # Users birthday input
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))

        # Create birthday object
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        # Calculate difference between today and birthday
        delta = today - birthday
        print(f'Difference is {delta.days} days')

        #Calculate age in years, months, weeks, and days
        delta_years = delta.days // 365.2425
        print(f'You are {delta_years} years old')

        delta_months = delta.days / 30.41  
        print(f"Or approximately {int(delta_months)} months old")

        delta_weeks = delta.days / 7  
        print(f"That's about {int(delta_weeks)} weeks old")

        # Print days (already calculated)
        print(f"And a total of {delta.days} days old")
       
      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()

# Run Program
main()