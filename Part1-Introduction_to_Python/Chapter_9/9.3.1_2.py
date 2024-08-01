data = ((1, 2), (3, 4))
print(data)

index = 1

for item in data:
    print(f"Row {index} sum: {sum(item)}")
    index += 1
