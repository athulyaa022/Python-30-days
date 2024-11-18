bill_amount=int(input("Enter the bill amount:"))
tip_percentage=int(input("Enter the tip percentage:"))
tip = (bill_amount*tip_percentage) / 100
total=bill_amount+tip
print("Tip amount:",tip)
print("Total amount to be paid:",total)