numbers = input("Enter numbers separated by spaces:")
numbers = numbers.split()
even_count = 0
odd_count = 0
for num in numbers:
    num = int(num)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")