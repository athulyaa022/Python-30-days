numbers=input("Enter numbers separated by spaces:")
numbers=numbers.split()
even_count=0
odd_count=0
for i in numbers:
    i=int(i)
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)