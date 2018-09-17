# import dog

class Animal:
    def __init__(self, name, sleepDuration):
        self.name = name
        self.sleepDuration = sleepDuration
    
    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleepDuration))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

myDog = Dog("Figs",7)
myDog.bark()
myDog.sleep()