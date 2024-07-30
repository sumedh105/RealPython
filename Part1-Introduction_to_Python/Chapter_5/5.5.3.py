num1 = input("Enter a number:")

num2 = input("Enter another number:")

num1 = float(num1)

num2 = float(num2)

diff = num1 - num2

is_integer = diff.is_integer()

print(f"The difference between {num1} and {num2} is an integer? {is_integer}!")
