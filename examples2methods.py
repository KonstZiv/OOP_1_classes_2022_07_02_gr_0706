class Dog:
    species = "familiars"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"*** {self.name} is {self.age} years old ***"
    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Sarik", 3)

dog2 = Dog("Dexter", 7)

#print(dog1.description())

print(dog2.speak("Bark"))

print(dog1)