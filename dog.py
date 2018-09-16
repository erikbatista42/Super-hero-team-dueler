dogs = list()
dogs.append("German Shepherd")
dogs.append("Poodle")
print(dogs)

class Dog: 
    def bark(self):
        print("Woof!")
# we can't do this. That's like telling all dogs to bark.
# Dog.bark() 

# instead, we want to tell tell an specific dog to bark.
myDog = Dog()
myDog.bark()
print(__name__)