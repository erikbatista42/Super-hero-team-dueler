# class Dog: 
#     # greeting = "Woof!"
#     name = "Spot"

#     def __init__(self, name):
#         # self.greeting = greeting
#         self.name = name

#     def bark(self):
#         print(self.name)
class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)

myFirstDog = Dog("Mel")
mySecondDog = Dog("Max")

print(myFirstDog.name)
print(mySecondDog.name)

myFirstDog.bark()
mySecondDog.bark()