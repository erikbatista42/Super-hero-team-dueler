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

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        # adds all abilities together to attack
        totalDamage = 0
        for ability in self.abilities:
            totalDamage += ability.attack()
        return totalDamage


    def takeDamage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        remainingHealth = self.currentHealth - damage
        self.currentHealth = remainingHealth
        # print("Current health: {}".format(self.currentHealth))

    def isAlive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.currentHealth > 0:
            return True
        else:
            return False


    def fight(self, opponent): # **** #
        '''
        Runs a loop to attack the opponent until someone dies.
        - Loop that both superheroes fight each other until someone dies
        '''
        while self.isAlive() or opponent.isAlive():

            heroAttack = self.attack()
            opponent.takeDamage(heroAttack)
            # print("{} currentHealth: {}".format(opponent.name, opponent.currentHealth))

            opponentAttack = opponent.attack()
            self.takeDamage(opponentAttack)
            # print("{} currentHealth: {}".format(self.name, self.currentHealth))

        if self.isAlive() == False:
            print("{} died".format(self.name))
        elif opponent.isAlive() == False:
            print("{} died".format(opponent.name))
        else:
            print("No one died...")


class Ability:
    def __init__(self, name, maxDamage):
        self.name = name
        self.maxDamage = maxDamage

    def attack(self):
        # Return a random attack value between 0 and max_damage.
        maxDamageRandomAttackValue = random.randint(0, self.maxDamage)
        return maxDamageRandomAttackValue

    def update_attack(self, newAttack):
        newAttack = self.maxDamage = newAttack
        return newAttack


class Weapon(Ability):
#returns random value between maxDamage & 1/2 of maxDamage
    def attack(self):
        randomValue = random.randint(self.maxDamage, self.maxDamage // 2)
        return randomValue


class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.team_name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(Hero)


    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        if name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)



if __name__ == "__main__":
    # superMan = Hero("Superman")
    # superManPunch = Ability("superman punch", 30)
    # superMan.addAbility(superManPunch)

    # batman = Hero("Batman")
    # kick = Ability("kick", 10)
    # batman.addAbility(kick)


    # superMan.fight(batman)
    hero = Hero("Wonder Woman")
    print(hero.attack()) # always 0 because has no abilities

    ability = Ability("Divine Speed", 30)
    hero.add_ability(ability)
    print(hero.attack()) # should be 1 - AbilityNum

    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack()) # should be 1 - AbilityNum

    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 800)
    hero2.add_ability(ability2)
    # print(hero2.attack())

    # hero.fight(hero2)
    teamOne = Team("losers")
    teamOne.add_hero(hero)
    teamOne.add_hero(hero2)
    teamOne.remove_hero(hero)
    teamOne.view_all_heroes()

    # teamTwo = Team("winners")

