def invest(amount, rate, years):
    for i in range(years):
        amount = amount * (1 + rate)
        print(f"year {i}: {amount:.2f}")

amount = input("Enter an initial amount:")
rate = input("Enter an annual percentage rate:")
years = input("Enter the number of years:")

res = invest(float(amount), float(rate), int(years))
