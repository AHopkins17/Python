
class Person:
    def __init__(self, name, address, age, phone) -> None:
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone: {self.__phone}"

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone(self, phone):
        self.__phone = phone
       
person = Person("Annette Hopkins", "123 Code, Python, USA", "34", "8152450086")

print(person.get_info())
print(person.get_name())
print(person.get_address())
print(person.get_age())
print(person.get_phone())

person1 = Person("Nettie Hopki", "321 Code, Python, USA", "33", "8159876543")
person2 = Person("Victoria Hopkins", "123456 Code, Python, USA", "35", "8151234567")
person3 = Person("Nettie Victoria", "987 Code, Python, USA", "36", "8151239876")

print(person1.get_info())
print(person1.get_name())
print(person1.get_address())
print(person1.get_age())
print(person1.get_phone())

print(person2.get_info())
print(person2.get_name())
print(person2.get_address())
print(person2.get_age())
print(person2.get_phone())

print(person3.get_info())
print(person3.get_name())
print(person3.get_address())
print(person3.get_age())
print(person3.get_phone())