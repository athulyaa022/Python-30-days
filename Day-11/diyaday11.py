num=input("Enter numbers separated by spaces:")
num=num.split()
even_count=0
odd_count=0
for number in num:
    number=int(number)
    if number % 2 == 0:
        even_count+=1
    else:
        odd_count += 1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)
