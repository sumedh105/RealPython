class Dog:
    species = "Canis familiarsis"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

dog = GoldenRetriever("gr", 20)
print(dog)
print(dog.speak())
