class Student:
    Total_number_of_Students = 25

    def __init__(self, roll_number, class_): #This is constructor taking values self argument will take the object here auto
        self.roll_number = roll_number;
        self.class_ = class_

    def DetailProvider(self):
        return f"Name is {self} roll number is {self.roll_number} and class is {self.class_}"

    @classmethod  #This Method will help me to change the number original class value
    def Changer_number_of_Students(cls, new_numbers):
        cls.Total_number_of_Students = new_numbers

Hammad = Student(6,"BSCS"); #Here Self parameter take Hammad automatically and 2nd one is rollnunber 3td is class we provided
print(Hammad.DetailProvider())
print(Hammad.Total_number_of_Students)
Hammad.Total_number_of_Students =5  #it will override all values if I comment it the last print show the change value by class method
print(Hammad.Total_number_of_Students)
Hammad.Changer_number_of_Students(95)
print(Hammad.Total_number_of_Students)