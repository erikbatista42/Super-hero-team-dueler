class Tiger(object):
    '''A tiger has a name, age and a favorite food.'''
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.favoriteFood = "sugar"

    def __str__(self):
        return "{0} is {1} years old".format(self.name, self.age)

tony = Tiger("Tony", 66)
# tony = Tiger.__init__(self, "Tony",66) What it's actually doing
# print("{0} is {1} years old".format(tony.name, tony.age))

hobbes = Tiger("Hobbes")
# print("{0} is {1} years old".format(hobbes.name, hobbes.age))
# print("#{name} is {0} years old".format( hobbes.age))
print(hobbes.favoriteFood)


# fight method

class Hero:
    def fight(self, opponent):
        '''Runs a loop to attack oppponent until someone dies'''
        while self.is_alive() or opponent.is_alive():




batman = Hero("batman")
wonderWoman = Hero("wonder Woman")

