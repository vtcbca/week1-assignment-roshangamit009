def a(number):
    number_str = str(number)
    b = 0
    for digit in number_str:
        b += int(digit)
    return b
number = int(input("Enter a number: "))
sum_of_digits = a(number)
print("The sum of the digits is:", sum_of_digits)
