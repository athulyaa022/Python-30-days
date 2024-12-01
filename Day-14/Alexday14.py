'''
Author:Alex
Date:1-12-2024
Description:Generate a Multiplication Table
'''
num1=int(input("Enter the number on which you want multiplication table: "))
print("Multiplication table for:",num1)
for i in range(1,11):
     result=num1*i
     print(num1,"*",i,"=",result)
