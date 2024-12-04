numbers = (10, 20, 30, 40, 50)
print("The tuple is:", numbers)
num = int(input("Enter a number to check if it exists in the tuple: "))
if num in numbers:
    print(f"The number {num} is at index {numbers.index(num)}.")
else:
    print(f"The number {num} is not in the tuple.")
max_num = max(numbers)
min_num = min(numbers)
print(f"The maximum number in the tuple is: {max_num}")
print(f"The minimum number in the tuple is: {min_num}")