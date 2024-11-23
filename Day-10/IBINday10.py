limit=int(input("Enter a number:"))
if limit<=0:
    print("enter a number greater than 0.")
else:
    total_sum=0
    i=1
    while i<= limit:
        total_sum=total_sum+i
        i=i+1
    print(f"The sum of numbers from 1 to  {limit} is : {total_sum}")
