# Daily Heart Rate Tracker

# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Empty list to store heart rate data
heart_rates = []

# User input for heart rate
for time_slot in time_slots:
    while True:
            heart_rate = int(input(f"Enter your heart rate (BPM) in the {time_slot}: "))
            break

    # Append time slot and corresponding heart rate to list
    heart_rates.append([time_slot, heart_rate])

# Calculate total
total_heart_rate = 0
for entry in heart_rates:
    total_heart_rate += entry[1] # Heart rate

# Calculate average heart rate
average_heart_rate = total_heart_rate / len(heart_rates)

# Print average heart rate
print(f"Average heart rate today: {average_heart_rate:.2f} BPM")


