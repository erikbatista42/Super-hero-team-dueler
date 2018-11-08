import random


class Hero:
    def __init__(self, name, startingHealth=100):

        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.startingHealth = startingHealth
        self.currentHealth = startingHealth
        self.abilities = list()

    def addAbility(self, ability):
        ''' Add ability to abilities list '''
        ability.append(self.abilities)

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        totalDamage = 0
        for ability in self.abilities:
            totalDamage += ability.attack()
        return totalDamage



    def takeDamage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        remainingHealth = self.currentHealth - self.damage
        self.currentHealth = remainingHealth
        print(self.currentHealth)

    def isAlive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if hero.isAlive:
            return True
        else:
            return False

    def fight(self, opponent): # **** #
        '''
        Runs a loop to attack the opponent until someone dies.
        - Loop that both superheroes fight each other until someone dies
        '''
        while hero.currentHealth > 0 or opponent.currentHealth > 0:
            # hero attack opponent
            # opponent takes damage and opponent's health decreases


            # opponent attacks hero
            # hero takes damage and hero's health decreases


            print("{} died".fomat(hero.name)) # print heroe's death when he dies


class Ability:
    def __init__(self, name, maxDamage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        self.name = name
        self.maxDamage = maxDamage

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        randomAttackValue = random.randint(0, self.maxDamage)
        return randomAttackValue


if __name__ == "__main__":
    heroOne = Hero()
