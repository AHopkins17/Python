#Part 1
# Employee class with attributes
class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# Get method
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    
# Set method
    def set_name(self, name):
        self.name = name
    def set_number(self, number):
        self.number = number

# ProductionWorker Subclass
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

# Get method
    def get_shift_number(self):
        return self.shift_number
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    
# Set method
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

# Shift type 
    def get_shift_type(self):
        return "Day" if self.shift_number == 1 else "Night"

# Part 2
# Prompt
def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for day, 2 for night): "))

# ProductionWorker Instance
    worker = ProductionWorker(name, number, shift_number, pay_rate)

# Display 
    print("\n-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print(f"Name : {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Shift: {worker.get_shift_type()}")
    print(f"Pay Rate: {worker.get_hourly_pay_rate():.2f}")
    print("-------------------------------------------------------")

# Run main function
if __name__ == "__main__":
    main()

