# Task 2
# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.

def ask_input():
    '''asks user for two integers and return them'''
    while True:
        try:
            input_1 = int(input("Enter first number : "))
            input_2 = int(input("Enter second number : "))
            return input_1,input_2
        except ValueError:
            print('please enter integers only!!')
            print()
def menu():
    '''displays menu and return choosed option'''
    option = input("A.Addition B.Subtraction C.Multiplication\nD.Division E.Modulus F.Exponentiation\nG.Exit\nChoose option : ")
    return option
def calculator():
    '''
    gives user options to choose operation
    based on choosed operation 
    performs the operation 
    prints the result of the operation
    '''
    choice = menu().upper()
    flag = True
    if(choice == "A"):
        num_1,num_2 = ask_input()
        result = num_1 + num_2
        operation = "Addition"
    elif(choice == "B"):
        num_1,num_2 = ask_input()
        result = num_1 - num_2
        operation = "Subtraction"
    elif(choice == "C"):
        num_1,num_2 = ask_input()
        result = num_1 * num_2
        operation = "Multiplication"
    elif(choice == "D"):
        num_1,num_2 = ask_input()
        if num_2 == 0:
            print("Mathematical Error!! Can't divide with zero.")
            print()
            flag = False
        else:
            result = round((num_1 / num_2),2)
            operation = "Division"
    elif(choice == "E"):
        num_1,num_2 = ask_input()
        if num_2 == 0:
            print("Mathematical Error!! Can't divide with zero.")
            print()
            flag = False
        else:
            result = num_1 % num_2
            operation = "Modulus"
    elif(choice == "F"):
        num_1,num_2 = ask_input()
        result = num_1 ** num_2
        operation = "Exponentiation"

    elif(choice == "G"):
        exit()
    else:
        print("Invalid User input")
        print()
        flag = False
    if(flag):
        print(f"{operation} = {result}")
        print()
    calculator()
print("-----------------Calculator-----------------")
calculator()