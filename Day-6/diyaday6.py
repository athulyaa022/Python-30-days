bill_amt=int(input("Enter bill amount:"))
tip_per=int(input("Enter the tip percentage:"))
tip = (bill_amt * tip_per) / 100
total=bill_amt+tip
print("Tip amount:",tip)
print("Total amount to be paid:",total)
