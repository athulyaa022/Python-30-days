bill_amount=int(input("Enter the bill amount:"))
tip_per=int(input("Enter the tip percentage:"))
tip=(bill_amount*tip_per)/100
total_bill=(bill_amount+tip)
print("Tip amount:",tip)
print("Total amount to be paid:",total_bill)