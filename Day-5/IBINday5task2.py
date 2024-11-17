first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
operator=input("Choose an operater (+, -, *, /):")
if operator=="+":
    print("The result is:",first_number+second_number)
elif operator=="-":
    print("The result is:",second_number-first_number)
elif operator=="*":
    print("The result is:",first_number*second_number)
elif operator=="/":
    print("The result is:",second_number/first_number)
else:
    print("invalid operator")