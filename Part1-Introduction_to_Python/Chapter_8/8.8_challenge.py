import random

num_of_trials = 10000
flips = 0

def coin_flip():
    if (random.randint(0, 1) == 0):
        return "heads"
    else:
        return "tails"
    
for i in range(num_of_trials):
    if (coin_flip() == "heads"):
        flips = flips + 1
        while (coin_flip() == "heads"):
            flips = flips + 1

        flips = flips + 1
    else:
        flips = flips + 1
        while (coin_flip() == "tails"):
            flips = flips + 1

        flips = flips + 1

average_flips = flips / num_of_trials
print(f"Average number of flips is: {average_flips}")




