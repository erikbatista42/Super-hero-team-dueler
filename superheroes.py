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
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        pass

    def takeDamage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        pass

    def isAlive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        pass

    def fight(self, opponent):
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass

class Ability:
    def __init__(self, name, maxDamage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        pass

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    pass
