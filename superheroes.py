import random


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        highestAttackVal = 400
        lowestAttackVal = highestAttackVal // 2
        randomAttackVal = random.randint(lowestAttackVal, highestAttackVal)
        return randomAttackVal

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Armor:

    def __init__(self, name, defense):
        # Instantiate name and defense strength.
        self.name = name
        self.defense = defense

    def defend(self):
        # Return a random value between 0 and the
        # Initialized defend strength.
        defendRandomVal = random.randint(0, self.defense)


class Hero(Ability):

    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):

        # This method should run the defend method on each piece of armor and calculate the total defense.
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.
        print("armor list: ")
        # print(self.armors)
        if self.health == 0:
            return 0

    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the hero's health.
        # If the hero dies update number of deaths.
        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        # self.kills += num_kills
        print(123)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total = 0
        for attack_with_abilities in self.abilities:
            total += Ability.attack(attack_with_abilities)
        return total


class Weapon(Ability):

    def attack(self):
        randomVal = random.randint(0, self.attack_strength)
        return randomVal


class Team(Hero):

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.teamKills = 0

    def add_hero(self, Hero):
        self.heroes.append(Hero)
        retStr = "Added {0}".format(Hero.name)
        return retStr

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[self.heroes.index(hero)]
                retStr = "Deleted {0}".format(name)
                return retStr
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                retStr = "{0} exists".format(hero.name)
                return retStr
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print("{0} is in {1}".format(hero.name, self.name))

    def attack(self, other_team):
        # This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        # It should call add_kill() on each hero with the number of kills made.
        totalAttackVal = 0
        for hero in self.heroes:
            print(hero.name)
            totalAttackVal += hero.attack()
        kills = other_team.defend(totalAttackVal)
        # self.teamKills += kills
        for myHeroes in self.heroes:
            myHeroes.add_kill(kills)
        print("Total team attack: {0} ".format(totalAttackVal))

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        # Return number of heroes killed in attack.
        defendVal = 0
        for hero in self.heroes:
            # defendVal += hero.defend()
            print("")

    def deal_damage(self, damage):
        # Divide the total damage amongst all heroes.
        # Return the number of heros that died in attack.
        numOfDeaths = 0
        caluclateDamage = damage / len(self.heroes)
        for hero in self.heroes:
            numOfDeaths += hero.take_damage(caluclateDamage)
        return numOfDeaths

    def revive_heroes(self, health=100):
        # This method should reset all heroes health to their original starting value.
        self.health = health
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        # This method should print the ratio of kills/deaths for each member of the team to the screen.
        # This data must be output to the terminal.
        print("SHOWING STATS")
        print(self.name)
        for hero in self.heroes:
            print("HERO: {0}".format(self.name))
        ability_names = []
        for ability in self.abilities:
            ability_names.append(ability.name)
        print("Abilities: " + ", ".join(ability_names))
        print("kills: {0} , deaths: {1}".format(self.kills, self.deaths))

    def update_kills(self):
        # this method should update each hero when there is a team kill
        print("updated kills:")
        print(self.teamKills)
        return self.teamKills


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        # This method should allow a user to build team one.
        print(123)

    def build_team_two(self):
        # This method should allow user to build team two.
        print(123)

    def team_battle(self):
        # This method should continue to battle teams until one or both teams are dead.
        print(123)

    def show_stats(self):
        # This method should print out the battle statistics including each heroes kill/death ratio.
        print(123)


if __name__ == "__main__":

    # Wonder Woman
    heroOne = Hero("Wonder Woman")
    # print(heroOne.name)
    punchAbility = Ability("Punch", 500)
    heroOne.add_ability(punchAbility)
    lightArmor = Armor("light armor", 200)
    heroOne.add_armor(lightArmor)
    # print(heroOne.)
    # print("Wonder Woman is attacking:")
    # print(heroOne.attack())

    # Superman
    heroTwo = Hero("Superman")
    # print(heroTwo.name)
    superPunch = Ability("Superman Punch", 700)
    heroTwo.add_ability(superPunch)
    mediumArmor = Armor("mediumArmor", 200)
    heroTwo.add_armor(mediumArmor)
    # print("Superman is attacking:")
    # print(heroTwo.attack())
    print(heroOne.defend())

    # Batman
    heroThree = Hero("Batman")
    # print(heroThree.name)
    headBumb = Ability("Head bumb", 500)
    heroThree.add_ability(headBumb)
    # print("Batman is attacking:")
    # print(heroThree.attack())

    # Super Chicken
    heroFour = Hero("Super Chicken")
    flapWings = Ability("Flap wings", 8000)
    heroFour.add_ability(flapWings)
    # print("Super Chicken is attacking:")
    # print(heroFour.attack())

    # # Shotgun weapon
    weaponOne = Weapon("Shotgun", 1000)

    # print(weaponOne.name)
    # print(weaponOne.attack_strength)
    # print("Weapons is attacking:")
    # print(weaponOne.attack())

    # Losers Team
    teamOne = Team("Losers")
    teamOne.add_hero(heroTwo)
    teamOne.add_hero(heroThree)
    # teamOne.view_all_heroes()

    # Winners Team
    teamTwo = Team("Winners")
    teamTwo.add_hero(heroOne)
    teamTwo.add_hero(heroFour)
    # teamTwo.view_all_heroes()
    # print("Trying to add all heroes attacks:")
    # print(heroOne.attack() + heroTwo.attack())
    teamTwo.attack(teamTwo)
