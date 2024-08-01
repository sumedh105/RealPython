class Animal:
    def __init__(self, name, sound, no_of_legs, is_wild):
        self.name = name
        self.sound = sound
        self.no_of_legs = no_of_legs
        self.is_wild = is_wild

    def __str__(self):
        return f"The animal {self.name} is a {self.is_wild} animal with {self.no_of_legs} legs and with sound {self.sound}"
    
class Lion(Animal):
    pass

lion = Lion("Lion", "Whow", 4, "wild")
print(lion)

class Tiger(Animal):
    pass

tiger = Tiger("Tiger", "Whow", 4, "wild")
print(tiger)

class Cow(Animal):
    pass

cow = Cow("Cow", "Hamba", 4, "not a wild")
print(cow)

