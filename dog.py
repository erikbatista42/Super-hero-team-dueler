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

my_dog = Dog("Mel")
print(my_dog.name)
my_dog.bark()

