class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

    def drive(self, no_of_miles):
        self.mileage += no_of_miles

bcar = Car("blue", 0)
print(bcar)

bcar.drive(100)
print(bcar)
