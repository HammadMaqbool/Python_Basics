class Student:
    class_room_common_for_all_instance =  "Room102"

    def DetailShows(self):
        return f"Roll Number is {self.roll_number} Class is {self._class} Class room is {self.class_room_common_for_all_instance}"


Hammad = Student()  # Here hammad is the object of class student
Sajid = Student() # Here Sajid is the 2nd object of the class student

#These are the instance variables means the varriables of the instance(object) Hammad
#Same we can do this for the object Sajid of class student
Hammad.roll_number = "06"
Hammad._class = "BSCS"
Hammad.Semester = "6th"

print(Hammad.roll_number)
print(Hammad.class_room_common_for_all_instance)
Hammad.class_room_common_for_all_instance = "Room_108"
print(Hammad.class_room_common_for_all_instance)
print(Sajid.class_room_common_for_all_instance)
print(Hammad.DetailShows())

