'''
Author:Alex
Date:27-11-2024
Description:Write a program to calculate the sum of the digits of a number.
'''
num_1=int(input("Enter a Positive Integer: "))
sum=0
while num_1>0:
    digit= num_1%10
    sum+=digit
    num_1//=10
print("The Sum of digits is: ",sum)