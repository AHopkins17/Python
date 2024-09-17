# Store names into a list
names = []

# Accept five names from the user
print("Please enter five names:")
for _ in range(5):
    name = input("Enter a name: ")
    names.append(name)

# Sorting the list using Bubble Sort
swapped = True
while swapped: 
    swapped = False # Reset  the flag at the start of each iteration
    for i in range(len(names) - 1): #Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True # A swap is needed
            # Swap elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print("\nSorted list of names:")
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print("\nReversed list of names:")
print(names)



