num1=int(input("Enter the start of the range:"))
num2=int(input("Enter the end of the range:"))
for n in range(num1,num2+1):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
