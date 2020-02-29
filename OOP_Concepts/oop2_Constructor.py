class Student:
    def __init__(self, roll_number, class_): #This is constructor taking values self argument will take the object here auto
        self.roll_number = roll_number;
        self.class_ = class_

    def DetailProvider(self):
        return f"Name is {self} roll number is {self.roll_number} and class is {self.class_}"

Hammad = Student(6,"BSCS"); #Here Self parameter take Hammad automatically and 2nd one is rollnunber 3td is class we provided

print(Hammad.DetailProvider())