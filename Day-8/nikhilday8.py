number1=int(input("Enter the start of the range:"))
number2=int(input("Enter the end of the range:"))
for i in range(number1,number2+1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")