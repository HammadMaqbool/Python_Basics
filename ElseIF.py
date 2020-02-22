# number_1= 10
# number_2 = 20
#
# #number_1,number_2 = number_2,number_1
#
# if number_1>number_2:
#     print(str(number_1) + " is greater this is if")
# else:
#     print(str(number_2) + " Is greater this is else")

age = int(input("Enter Your age"))
if age > 7 and age <100:
    if age>18 and age<=80:
        print("Yes you can drive")
    elif age ==18:
        print("We will think over it")
    elif age > 80:
        print("Its not safe for you to drive a car")
else:
    print("invalid age to use computer")
