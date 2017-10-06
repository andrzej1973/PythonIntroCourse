#!/usr/bin/python

def add(num1,num2):
    """Return sum of num1 and num2"""
    return num1 + num2

def sub(num1,num2):
    """Return substraction of num2 from num1"""
    return num1-num2

def mul(num1,num2):
    """Return multiplication of num1 and num2"""
    return num1*num2

def div(num1,num2):
    """Returns division of num1 over num2"""
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Division by 0 not allowed, returning 0...")
        return 0


def ExecuteOperation(operation, number1,number2):
    """Executes operation specified in int operation and
    executes it over num1 and num2"""
    if (operation == 1 or operation=='+'):  # 1 means add
        print("The sum is:", add(number1, number2))
    elif (operation == 2 or operation=='-'):  # 2 means substract
        print("The substraction is:", sub(number1, number2))
    elif (operation == 3 or operation=='*'):  # 3 means multiply
        print("The multiplication is:", mul(number1, number2))
    elif (operation == 4 or operation=='/'):  # 4 means divide
        print("The division is:", div(number1, number2))
    else:  # catch unsupported requests
        print("Unsuported request")

def main():
    AnotherOperation="Y"
    while (AnotherOperation=='Y' or AnotherOperation=='y'):
        SupportedArgument = False
        while (SupportedArgument==False):
            try:
                num1=int(input ("what is number 1?"))
                num2=int(input ("what is number 2?"))
                operation=int(input("what do you want to do? ( 1) add, 2) substract, "
                                    "3) multiply, 4) divide)"))
                SupportedArgument=True
            except ValueError:
                print("unsuported argument, please try again...")
                SupportedArgument=False

        ExecuteOperation(operation,num1,num2)
        AnotherOperation = str(input("Do you want to continoue? Yes - Y, No - any other key"))
    print("See you...")


if __name__=="__main__":
    main()
