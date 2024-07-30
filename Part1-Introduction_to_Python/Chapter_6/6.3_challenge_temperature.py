def convert_cel_to_fahr(cel):
    fahr = (cel * (9 / 5)) + 32
    return fahr

def convert_fahr_to_cel(fahr):
    cel = (fahr - 32) * (5 / 9)
    return cel

fahr = input("Enter a temperature in degrees F:")
fahr_to_cel = convert_fahr_to_cel(float(fahr))
print(f"{fahr} degrees F = {fahr_to_cel:.2f} degrees C")

cel = input("Enter a temperature in degrees C:")
cel_to_fahr = convert_cel_to_fahr(float(cel))
print(f"{cel} degrees C = {cel_to_fahr:.2f} degrees F")

