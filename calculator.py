#Python clacualtor program
from email.headerregistry import Address
from subprocess import SubprocessError


#define function
def calculator(a,b):
    a = int(input("Enter the number a: "))
    b = int(input("Enter the number b: "))

    print("1.Addition",
          "2.Subtraction",
          "3.Multiplication",
          "4.Division",
          "5.Floor Division",
          "6.Percentage")
    choice = int(input("Enter the value of the choice: "))

    if choice == 1:
        result = a+b
        print (result)
    elif choice == 2:
        result = a-b
        print(result)
    elif choice == 3:
        result = a*b
        print(result)
    elif choice == 4:
        result = a/b
        print(result)
    elif choice == 5:
        result = a//b
        print(result)
    elif choice == 6:
        result =a%b
        print(result)
    else:
        print("invalid choice")

calculator('a' ,'b')

