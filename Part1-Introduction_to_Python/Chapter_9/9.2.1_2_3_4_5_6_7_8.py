food = ["rice", "beans"]
print(f"food = {food}")

food.append("broccoli")
print(f"food = {food}")

food.extend(("bread", "pizza"))
print(f"food = {food}")

print(food[:2])

print(food[-1:])

breakfast = "eggs, fruit, orange, juice".split()
print(f"breakfast = {breakfast}")

print(len(breakfast))

lengths = [len(item) for item in breakfast]
print(f"lengths = {lengths}")
