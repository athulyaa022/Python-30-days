'''
Author:Alex
Date:21-11-2024
Description: Write a program that asks the user to enter numbers one by one and
stops as soon as the user enters an odd number.
'''
num_1=int(input("Enter a number"))
while True:
    if num_1%2==0:
        num_1=int(input("Enter a number"))
    else:
        print("You entered an odd number")
        break


