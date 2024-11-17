number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
operator=input("Choose an operation (+, -, *, /):")
if operator=="+":
    print("The result is:",number1+number2)
elif operator=="-":
    print("The result is:",number2-number1)
elif operator=="*":
    print("The result is:",number1*number2)
elif operator=="/":
    print("The result is:",number2/number1)
else:
    print("invalid operator")