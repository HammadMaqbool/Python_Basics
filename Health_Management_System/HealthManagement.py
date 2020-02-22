
def fun_food_lock(p_name,food, DateToday):
    food_file_pointer = open("f_"+p_name.lower()+".txt", "a")
    food_file_pointer.write(str(DateToday)+"\n"+food+" \n")
    food_file_pointer.close()


def fun_exercise_lock(e_name, ex_done, DateToday):
    exercise_file_pointer = open("e_"+e_name.lower()+".txt", "w")
    exercise_file_pointer.write(str(DateToday) + "\n" + ex_done + " \n")
    exercise_file_pointer.close()

def fun_food_read(user_name):
    food_read_pointer = open("f_"+user_name.lower()+".txt", "r")
    content_read = food_read_pointer.read()
    food_read_pointer.close()
    return content_read

def fun_exercise_read(user_name):
    exercise_read_pointer = open("e_"+user_name.lower()+".txt", "r")
    content_exe = exercise_read_pointer.read()
    exercise_read_pointer.close()
    return content_exe

def DateTme_function():
    import  datetime
    temp = datetime.datetime.today()
    todayDate = temp.strftime("%x")
    return todayDate

get_user_name = input("Welcome\nMay I know who is there? | Hammad OR Sajid ")
print("What do you want to do? | Lock or Read?")
lock_read_choice = input()
if lock_read_choice == "lock" or lock_read_choice=="Lock" or lock_read_choice=="LOCK":
    lock_choice = input("What do you want to lock? | Food or Exercise?")

    if lock_choice == "food" or lock_choice == "FOOD" or lock_choice == "Food":
        food_choice = input("What you eat today?")
        DateToday = DateTme_function()
        fun_food_lock(get_user_name,food_choice,DateToday)
    elif lock_choice == "exercise" or lock_choice=="Exercise" or lock_choice=="EXERCISE":
        exercice_choice = input("What Exercise you did today "+get_user_name )
        DateToday = DateTme_function()
        fun_exercise_lock(get_user_name,exercice_choice,DateToday)

elif lock_read_choice=="Read" or lock_read_choice=="read" or lock_read_choice == "READ":
    read_choice = input("Which log do you want to read Mr."+get_user_name+" Your food or Exercise?")

    if read_choice == "food" or read_choice=="Food" or read_choice=="Food":
        food_log_read = fun_food_read(get_user_name)
        print("Mr."+get_user_name+"Here is Your food log\n")
        print(food_log_read)
    elif read_choice == "exercise" or read_choice == "Exercise" or read_choice=="EXERCISE":
        exercise_log =fun_exercise_read(get_user_name)
        print("Mr." + get_user_name + "Here is Your exercise log\n")
        print(exercise_log)
else:
    print("Wrong Choice")

