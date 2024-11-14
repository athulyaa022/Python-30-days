'''
Author:Alex
Date:14-11-2024
Description:The if statement lets you control the flow of your program based on conditions.
 Today, you’ll practice using if and if-else statements to categorize age groups based on user input.
'''
age=int(input("Enter your age"))
print(age)
if age<13 :
    print("You are a Child")
    age = int(input("Enter your age"))
    print(age)
if age>13 and  age<20 :
    print("you are teen")
    age = int(input("Enter your age"))
    print(age)
if age>20 and age<64 :
    print("you are adult")
    age = int(input("Enter your age"))
    print(age)
if(age>=65):
    print("you are a senior")
else:
    print("older")








