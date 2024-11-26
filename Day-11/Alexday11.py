'''
Author:Alex
Date:24-11-2024
Description:Write a program that counts the number of even and odd numbers in a list provided by the user.
'''
list_1=input("Enter numbers separated by spaces:")
list_1=list_1.split()
even_count=0
odd_count=0
num=0
for num in list_1:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
num+=1
print("Even numbers ",even_count)
print("Odd numbers ",odd_count)

