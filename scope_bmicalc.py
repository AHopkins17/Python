# BMI Calculator

# Global conversion
POUNDS_TO_KG = 0.453592     # 1 pound = 0.453592 kg
INCHES_TO_M = 0.0254        # 1 inch = 0.254 m

def is_positive_number(value):
    """Check if the value can be converted to a positive float."""
    try:
        num = float(value)
        return num > 0      # Check if it's positive
    except:
        return False        # If conversion fails, return False
    
def main():
    """ This function calculates and shows a user's BMI category based on their weight and height """

    # User weight and height input
    while True: 
        weight_input = input("Enter your weight in pounds: ")
        height_input = input("Enter your height in inches: ")

        # Checking for positive numerical values
        if is_positive_number(weight_input) and is_positive_number(height_input):
            weight_lbs = float(weight_input)
            height_in = float(height_input)

        # Conversion to metric Units
            weight_kg = weight_lbs * POUNDS_TO_KG
            height_m = height_in * INCHES_TO_M

        # BMI calculation
            bmi = weight_kg / (height_m * height_m)

        # BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
            
        # Results Display
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the {category} category.")
        break
    else:
        print("Invalid input. Please enter valid numbers for weight(lbs) and height(inches).")

# Call main function
if __name__ == "__main__":
    main()

    