bill = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip = (bill * tip_percentage) / 100
total_amount = bill + tip
print("Tip amount:", tip)
print("Total amount to be paid:", total_amount)
