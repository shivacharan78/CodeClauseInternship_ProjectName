from functions import *
print("Select the operator:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice= input("Enter your choice:")
num1=float(input("Enter the Number 1 : "))
num2=float(input("Enter the Number 2 : "))
if choice == '1':
    addition(num1,num2)
elif choice == '2':
    subtraction(num1,num2)
elif choice == '3':
    multiplition(num1,num2)
elif choice == '4':
    division(num1,num2)
else:
    print("Invalid Input!!")