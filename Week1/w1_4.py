#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
def arm(number):
    no = str(number)
    no_d = len(no)
    digit_sum = 0
    for digit in no:
        digit_sum += int(digit) ** no_d
    if digit_sum == number:
        return True
    else:
        return False
number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    if arm(number):
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")
else:
    print("Invalid input. Please enter an integer number.")
