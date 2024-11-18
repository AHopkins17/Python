# Define Pet class
class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

# Get methods
    def get_kind(self):
        return self.kind
    def get_breed(self):
        return self.breed
    def get_name(self):
        return self.name
# Set Methods
    def set_kind(self, kind):
        self.kind = kind
    def set_breed(self, breed):
        self.breed = breed
    def set_name(self, name):
        self.name = name
# Print details method
    def print_details(self):
        print(f"Kind: {self.kind}, Breed: {self.breed}, Name: {self.name}")

# Creating Instances
pet1 = Pet("Dog", "Frenchie", "Freya")
pet2 = Pet("Cat", "Persian", "Sophia")
pet3 = Pet("Bird", "Parrot", "Cash")

# Call print_details method
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Using getattr() to access an attribute of Pet instance
print(getattr(pet2, 'breed')) 

