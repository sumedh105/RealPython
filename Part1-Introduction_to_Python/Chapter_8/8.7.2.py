import random

res = 0

def roll():
    return random.randint(1, 6)

for i in range(1, 10000):
    res = res + roll()
    res = res / 10000

print(f"{res:.6f} is the average number")
