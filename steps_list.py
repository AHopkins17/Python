# Create a list of days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize an empty list for steps
steps = []

# User input, using a loop
for i in range(len(days)):
    # Ask user to input the number of steps on current day
    user_input = input(f"How many steps did you take on {days[i]}? ")

    step_count = int(user_input)

    # Append input to the 'steps' list
    steps.append(step_count)

# Display Daily Steps
print("\n")
for i in range(len(days)):
    print(f"You took {steps[i]} steps on {days[i]}")

# Total Steps
total_steps = sum(steps)
print(f"\nTotal steps: {total_steps}")

#Average Steps
average = round(total_steps / len(steps))
print(f"Average steps: {average}")