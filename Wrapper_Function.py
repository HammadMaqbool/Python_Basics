def Decorator_Func(any_function):
    def Functionality_Enhancer():
        print("This is the line from enhancer\n")
        any_function()
        print("This is the awsumm function")
    return Functionality_Enhancer

@Decorator_Func
def Function_1():
    print("This is the function 1\n")

Function_1()


var = Decorator_Func(Function_1)
var()

