from pywebio.input import *
from pywebio.output import *
def calculator():
    first = input("Enter the first number:",type = FLOAT)
    Second = input("Enter the second number:",type = FLOAT)
    c=0
    operation = radio("Choose one operation", options=["+","-","*","/"])
    operation_name = ""
    if operation == "+":
        operation_name ="Addition"
        c = first+Second

    elif operation == "-":
        operation_name = "Subtraction"
        c = first-Second
    
    elif operation == "/":
        operation_name = "division"
        c = first/Second
    
    elif operation == "*":    
        operation_name = "Multiplication"
        c = first*Second
        
    put_text("Operation Selected is: %s and the output is: %.1f" %(operation_name,c))
    
if __name__ == "__main__":
    calculator()