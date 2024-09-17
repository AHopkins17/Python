# Initialize Seating List 1 to 20
seats = list(range(1, 21))

# Display Available Seats
print("Available seats:", seats)

# Implement the Ticket Purchase Process
while True:
    # Promt the customer to select a seat or finish their purchase
    seat_choice = int(input("Please enter seat number to purchase or 0 to finish: "))

    if seat_choice == 0:
        print("Thank you for your purchase!")
        break
    elif seat_choice in seats:
        seats.remove(seat_choice)  # Update seat availability
        print(f"Seat {seat_choice} has been successfully purchased.")
    else:
        print("Seat is already taken. Please try a different seat number.")

    # Display updated list of available seats
    print("Available seats:", seats)

