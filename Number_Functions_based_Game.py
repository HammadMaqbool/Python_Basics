import random
Comp_guess_number = random.randint(1,5)
total_number_of_Attempts = 3
cuurent_attempt =1
# Note: Ffunction_name.__doc__ is a method use to read the doc string of the function.
def remining_attempts_checker():
    """It checks every time how much attempts remaining"""
    if cuurent_attempt == total_number_of_Attempts:
        print("This is last attempt")

def user_input_guess():
    """It takes input from the user"""
    User_guess = int(input("Enter your guess this is attempt number " + str(cuurent_attempt) + "\n"))
    return User_guess

while(cuurent_attempt<=total_number_of_Attempts):
    remining_attempts_checker()
    User_guess_value = user_input_guess()

    cuurent_attempt = cuurent_attempt + 1
    if User_guess_value>Comp_guess_number:
        if cuurent_attempt == total_number_of_Attempts+1:
            print("This was last attempt you failed game over!\n Number was "+str(Comp_guess_number))
        else:
            print("Try small number")
        continue
    elif User_guess_value<Comp_guess_number:
        if cuurent_attempt == total_number_of_Attempts+1:
            print("This was last attempt you failed game over!\n Number was "+str(Comp_guess_number))
        else:
            print("Try large number")
        continue
    else:
        print("Congratulations Number matched in "+str(cuurent_attempt-1)+" attempts")
        break
