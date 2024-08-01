class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

bcar = Car("blue", 20000)
rcar = Car("red", 30000)

print(bcar)
print(rcar)

