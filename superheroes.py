import random


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.starting_health = health
        self.current_health = health
        self.abilities = list() # list of abilities and weapons
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        ''' adds all abilities together to attack '''
        totalDamage = 0
        for ability in self.abilities:
            totalDamage += ability.attack()
        return totalDamage


    def take_damage(self, damage):
        self.health -= damage - self.defend()


    def defend(self):
        ''' Runs block method on each armor to calculate totalDefense '''
        totalDefense = 0
        for armor in self.armors:
            totalDefense += armor.block()

        if self.health <= 0:
            self.deaths += 1
            totalDefense = 0
        return totalDefense


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        self.kills += num_kills

    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():

            heroAttack = self.attack()
            opponent.take_damage(heroAttack)

            opponentAttack = opponent.attack()
            self.take_damage(opponentAttack)

            if self.is_alive() == False:
                print("{} died".format(self.name))
                opponent.add_kill(1)
                self.deaths += 1
            elif opponent.is_alive() == False:
                print("{} died".format(opponent.name))
                self.add_kill(1)
                opponent.deaths += 1





class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        randomAttackValue = random.randint(0, self.attack_strength)
        return randomAttackValue

    def update_attack(self, new_attack_strength):
        newAttackStrengthValue = self.randrange(attack_strength, new_attack_strength)
        return newAttackStrengthValue


class Weapon(Ability):

    def attack(self):
        randomAttackValue = random.randint(self.attack_strength // 2, self.attack_strength)
        return randomAttackValue


class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = list()


    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):

        for hero in self.heroes:
            if hero.name == name:
                indexOfHero = self.heroes.index(hero)
                del self.heroes[indexOfHero]
                return
        ''' did not find hero so give an error value '''
        return 0


    def view_all_heroes(self):
        ''' Prints all heroes to the console '''
        for hero in self.heroes:
            print(hero.name)


    def attack(self, other_team):

        randomElement = random.SystemRandom()

        ''' randomly select a living hero from each '''
        selfRandomHero = randomElement.choice(self.heroes)
        other_team_random_hero = randomElement.choice(other_team.heroes)

        ''' Fight until one or both teams have no surviving heroes '''
        while other_team_random_hero.current_health > 0:
            selfRandomHero.fight(other_team_random_hero)
            other_team_random_hero.current_health -= 1


    def revive_heroes(self, health=100):
        ''' Resets all heroes health to their original starting value.'''
        for hero in self.heroes:
            hero.health = health

    def stats(self):
        ''' Prints Kills/Deaths ratio for each hero'''
        for hero in team.heroes:
            kdr = hero.kills / hero.deaths
            print("{}'s K/D: {}".format(hero.name, kdr))


class Armor:

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        randomValue = random.randint(0, self.max_block)
        return randomValue


if __name__ == "__main__":


 ''' *** Shout out to Ramon for helping me with this project *** '''

