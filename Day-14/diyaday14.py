num=int(input("Enter a number to generate its multiplication table:"))
print("Multiplication table for",num,":")
for number in range(1,11):
    result=num*number
    print(num,"*",number,"=",result)
