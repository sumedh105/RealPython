integer = int(input("Enter a positive integer:"))

i = 1

for i in range(1, integer+1):
    if (integer%i == 0):
        print(f"{i} is a factor of {integer}")
