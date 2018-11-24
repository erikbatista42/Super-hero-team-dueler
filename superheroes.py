import random


class Hero:
    def __init__(self, name, health=100):

        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.health = health
        self.starting_health = health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

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

        # REFACTOR INSTRUCTIONS
        '''
        Refactor this method to use the new defend method and to update the number of deaths if the hero dies in the attack.
        '''
        self.health -= damage - self.defend()


    def defend(self):
        # This method should run the defend method on each piece of armor
        # and calculate the total defense.
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.

        totalDefense = 0
        for armor in self.armors:
            totalDefense += armor.block()

        if self.health <= 0:
            #  hero is out of play
            # and should return 0 defense points.
            self.deaths += 1
            totalDefense = 0
        return totalDefense


    def is_alive(self):
    #This function will return true if the hero is alive or false if they are not.
        if self.health > 0:
            return True
        else:
            return False


    def fight(self, opponent): # **** #
        '''
        Runs a loop to attack the opponent until someone dies.
        - Loop that both superheroes fight each other until someone dies
        '''

        '''
        Refactor this method to update the number of kills the hero has when the opponent dies.
        '''

        while self.is_alive() and opponent.is_alive():

            heroAttack = self.attack()
            opponent.takeDamage(heroAttack)
            # print("{} currentHealth: {}".format(opponent.name, opponent.currentHealth))

            opponentAttack = opponent.attack()
            self.takeDamage(opponentAttack)
            # print("{} currentHealth: {}".format(self.name, self.currentHealth))

        if self.is_alive() == False:
            print("{} died".format(self.name))
            self.add_kill(1)
        elif opponent.is_alive() == False:
            print("{} died".format(opponent.name))
            opponent.add_kill(1)

    def add_kill(self, num_kills):
        '''
        This method should add the number of kills to self.kills
        '''
        self.kills += num_kills


class Ability:


    def __init__(self, name, attack_strength):
        ''' Initialize starting values '''
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        '''
         Return attack value
         between 0 and the full attack.
         '''
        randomAttackVal = random.randint(0, self.attack_strength)
        return randomAttackVal

    def update_attack(self, new_attack_strength):
        newAttackStrengthVal = self.randrange(attack_strength, new_attack_strength)
        return newAttackStrengthVal


class Weapon(Ability):
    def attack(self):
        randomValue = random.randint(self.attack_strength // 2, self.attack_strength)
        return randomValue


class Team:
    def __init__(self, name):
        '''Instantiate resources.'''
        self.name = name
        self.heroes = list()

    def add_hero(self, Hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(Hero)


    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero.name == name:
                indexOfHero = self.heroes.index(hero)
                del self.heroes[indexOfHero]
                return
        # did not find hero so give an error value
        return 0


    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)


    def attack(self, other_team):
        # randomly select a living hero from each √
        # have them fight until one or both teams have no surviving heroes

        # Hint: Use the fight method in the Hero class.
        randomElement = random.SystemRandom()

        randomHero = randomElement.choice(self.heroes)
        other_team_random_hero = randomElement.choice(other_team.heroes)




    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        for hero in heroes:
            hero.health = health

    def stats(self):
        '''
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the console.
        '''
        for hero in team.heroes:
            # print("{} kills: {}".format(hero.name,hero.kills))
            # print("{} deaths: {}".format(hero.name,hero.deaths))
            kdr = hero.kills / hero.deaths
            print("{}'s K/D: {}".format(hero.name, dkr))

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        randomValue = random.randint(0, self.max_block)
        return randomValue


if __name__ == "__main__":
    # superMan = Hero("Superman")
    # superManPunch = Ability("superman punch", 30)
    # superMan.addAbility(superManPunch)

    # batman = Hero("Batman")
    # kick = Ability("kick", 10)
    # batman.addAbility(kick)


    # superMan.fight(batman)
    hero = Hero("Wonder Woman")
    # print(hero.attack()) # always 0 because has no abilities

    ability = Ability("Divine Speed", 30)
    hero.add_ability(ability)
    # print(hero.attack()) # should be 1 - AbilityNum

    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    # print(hero.attack()) # should be 1 - AbilityNum

    hero2 = Hero("Jodie Foster")
    ability2 = Ability("Science", 20)
    mediumArmor = Armor("Medium Armor", 400)
    hero2.add_ability(ability2)
    # print(hero2.attack())

    # hero.fight(hero2)
    teamOne = Team("losers")
    teamOne.add_hero(hero)
    teamOne.add_hero(hero2)
    teamOne.heroes[0].name = "Michael Jackson"
    teamOne.remove_hero("Michael Jackson")
    print("all heroes:")
    teamOne.view_all_heroes()
    # print(teamOne.heroes[0].name)

    teamTwo = Team("winners")

