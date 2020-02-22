#Basic dictionary. . .
my_dict = {"1":"one", "2":"two", "3":"Three", "4":"Four"}
chose_number = input("Enter the number")
print(my_dict[chose_number])

#Adding a new value to dictionary, taking input on same line
add_key,add_value = input("Enter a new number\nE.g: Key, value").split(",")
my_dict.update({add_key:add_value})

#Printing a dictionary
print(my_dict)

#Del Some dictionary value of user choice
value_to_del = input("Enter the key value you want to delete")
my_dict.pop(value_to_del)

#Printing final version of dicitionary
print(my_dict)