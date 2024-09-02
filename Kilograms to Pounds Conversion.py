# Define variables for kilograms values
kg_value_1 = 30.5
kg_value_2 = 72.6
kg_value_3 = 98.8
kg_value_4 = 110.5

# Conversion factor: 1 pound = 2.20 kilograms
conversion_factor = 2.20

# Calculate pounds for each kilograms value
pounds_1 = kg_value_1 / conversion_factor
pounds_2 = kg_value_2 / conversion_factor
pounds_3 = kg_value_3 / conversion_factor
pounds_4 = kg_value_4 / conversion_factor

# Output the results
print(f"{kg_value_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {pounds_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {pounds_4:.2f} pounds.")