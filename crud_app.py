# Main Menu Function
def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

# File Check Function
def check():
    try:
        with open("customer_list.txt", 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

# Save Function
def save(output):
    with open("customer_list.txt", 'w') as file:
        file.writelines(output)
    print("File updated.")

# Create Function
def create():
    customer = check()
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)
    print("New entry created.")

# Read Function
def read():
    customer = check()
    lname = input("Enter the last name of the customer you want to find: ")
    found = False
    for entry in customer:
        if lname.lower() in entry.lower():
            print("Found:", entry.strip())
            found = True
    if not found:
        print("No matching entry found.")

# Delete Function
def delete():
    customer = check()
    lname = input("Enter the last name of the customer you want to delete: ")
    updated_list = [entry for entry in customer if lname.lower() not in entry.lower()]

    if len(updated_list) != len(customer):
        save(updated_list)
        print("Entry deleted successfully.")
    else:
        print("No matching entry found.")

# Update Function
def update():
    customer = check()
    lname = input("Enter the last name of the customer you want to update: ")
    found = False

    for i in range(len(customer)):
        if lname.lower() in customer[i].lower():
            print("Current entry:", customer[i].strip())
            fname = input("Enter new first name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            customer[i] = f"{fname}, {lname}, {phone}, {email}\n"
            found = True
            save(customer)
            print("Entry updated successfully.")
            break

    if not found:
        print("No matching entry found.")

# Main Program
if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
