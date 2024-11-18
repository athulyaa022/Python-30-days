'''
Author:Alex
Date:18-11-2024
Description:This task will reinforce basic arithmetic and variable usage.
 You’ll ask the user for the bill amount and tip percentage, calculate the tip,
 and display the total amount to be paid.
'''
bill=int(input("Enter the bill amount: "))
tip_percentage=int(input("Enter the tip percentage"))
tip=(bill*tip_percentage)/100
Total_amount=bill+tip
print(tip)
print(Total_amount,"to be paid")