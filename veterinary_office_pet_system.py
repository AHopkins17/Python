# Define the Pet class
class Pet:
    
    vet_name = "Furbabies Veterinary Clinic"
    
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
       
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    
    
    def set_owner_first_name(self, first_name):
        self.__owner_first_name = first_name

    def get_owner_first_name(self):
        return self.__owner_first_name
    
    
    def set_owner_last_name(self, last_name):
        self.__owner_last_name = last_name

    def get_owner_last_name(self):
        return self.__owner_last_name
    
    
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def get_pet_id(self):
        return self.__pet_id
    
    
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def get_pet_name(self):
        return self.__pet_name
    
   
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def get_pet_type(self):
        return self.__pet_type
    
    
    def display_pet_info(self):
        print(f"Veterinary Office: {Pet.vet_name}")
        print(f"Owner: {self.get_owner_first_name()} {self.get_owner_last_name()}")
        print(f"Pet ID: {self.get_pet_id()}")
        print(f"Pet Name: {self.get_pet_name()}")
        print(f"Pet Type: {self.get_pet_type()}")
        print("-------------------------------")
    
# Property Existence Check hasattr()
    def check_property(self, property_name):
        return hasattr(self, f"_{self.__class__.__name__}__{property_name}")
    

# Create instances (objects) of the Pet class
pet1 = Pet("Jack", "Door", 100, "Roger", "Cat")
pet2 = Pet("Veronica", "Jacklin", 101, "Buddy", "Dog")
pet3 = Pet("Frank", "Wilson", 102, "Drake", "Dog")

# Use setter method to change a property for pet1
pet1.set_pet_name("Chopper")
pet1.set_pet_type("Dog")

# Display information
print("Displaying Pet Information:\n")
pet1.display_pet_info()
pet2.display_pet_info()
pet3.display_pet_info()

# Check property existence using check_property()
print("Checking if properties exist for pet1:")
print("Has 'owner_first_name' property:", pet1.check_property('owner_first_name'))
print("Has 'pet_color' property:", pet1.check_property('pet_color'))