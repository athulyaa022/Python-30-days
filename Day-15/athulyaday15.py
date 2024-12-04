start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
num = int(input("Enter the number to find multiples of: "))
total_sum = 0
for i in range(start, end + 1):
    if i % num == 0:
        total_sum += i
print(f"The sum of multiples of {num} between {start} and {end} is: {total_sum}")
