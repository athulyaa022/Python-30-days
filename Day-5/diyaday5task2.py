num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=input("Choose an operation(+, -, *, /):")
if operation=='+':
    final_result=num1+num2
    print("The result is:", final_result)
elif operation=='-':
    final_result=num1-num2
    print("The result is:", final_result)
elif operation=='*':
    final_result=num1*num2
    print("The result is:", final_result)
elif operation=="/":
    final_result=num1/num2
    print("The result is:", final_result)
else:
    print("Invalid Operator ")
