def is_harshad(num):
    # Find the sum of digits of the number
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Test the function with an example
number = int(input("Enter a number: "))
if is_harshad(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
