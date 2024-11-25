number=int(input("Enter a positive integer: "))
sum_of_the_digits=0
while number>0:
    last_digit=number%10
    sum_of_the_digits+=last_digit
    number//=10
print("The sum of the digits is:",sum_of_the_digits)