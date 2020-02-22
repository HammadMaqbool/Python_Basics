import random
Comp_guess_number = random.randint(1,5)
total_number_of_Attempts = 3
cuurent_attempt =1

while(cuurent_attempt<=total_number_of_Attempts):

    if cuurent_attempt == total_number_of_Attempts:
        print("This is last attempt")

    User_guess = int(input("Enter your guess this is attempt number "+str(cuurent_attempt)+"\n"))
    cuurent_attempt=cuurent_attempt+1
    if User_guess>Comp_guess_number:
        if cuurent_attempt == total_number_of_Attempts+1:
            print("This was last attempt you failed game over!\n Number was "+str(Comp_guess_number))
        else:
            print("Try small number")
        continue
    elif User_guess<Comp_guess_number:
        if cuurent_attempt == total_number_of_Attempts+1:
            print("This was last attempt you failed game over!\n Number was "+str(Comp_guess_number))
        else:
            print("Try large number")
        continue
    else:
        print("Congratulations Number matched in "+str(cuurent_attempt-1)+" attempts")
        break