num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=input("Choose an operation (+, -, *, /): ")
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    result=num1/num2
else:
    print("Invalid Operator")
print("The result is:",result)