class Person:
    Name = None     #None stand for nothing and use to declare a variable without any value.
    Age = None
    Address = None
    PhoneNumber = None

    def Get_Personaldetails(self):
        return f"The Name of this Person is {self.Name} and the age is {self.Age} " \
               f"the Address of this person is {self.Address} and the Phone number" \
               f"is {self.PhoneNumber}"

    @staticmethod
    def ToPrintWelcome(Name):
        return f"Welcome Mr.{Name}"

class Employee(Person):  #This is class employee extends to  person means the employee is child class of person
    def get_EmployeeDetaisl(self):
        return f"Employee Name is {self.Name} this is inherited from persom class"


Hammad = Employee()
Hammad.Name = "Hammad"
Hammad.PhoneNumber = 341
Hammad.Address = "Kotli"
Hammad.Age = 28

print(Hammad.ToPrintWelcome("Hammad"))
print(Hammad.Get_Personaldetails()) # The method is inherited from the person class
print(Hammad.get_EmployeeDetaisl()) # direct from the employee class
