'''
Author:Alex
Date:20-11-2024
Description: Write a program to identify and print all even and odd numbers within a specified range.
'''
num_1=int(input("Enter the start of the range"))
num_2=int(input("Enter the end of the range"))
print(num_1)
print(num_2)
for n in range(num_1,num_2+1):
    if n%2==0 :
        print(n,"is even")
    elif n%2!=0 :
        print(n,"is odd")
    else:
        print("invalid Entry")
