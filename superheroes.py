import random


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # highestAttackVal = 400
        # lowestAttackVal = highestAttackVal // 2
        # randomAttackVal = random.randint(lowestAttackVal, highestAttackVal)
        # return randomAttackVal
        random_int = random.randint(self.attack_strength // 2, self.attack_strength)
        return random_int

    def update_attack(self, new_attack_strength):
        self.attack_strength = new_attack_strength


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
        # print("armor list: ")
        # print(self.armors)

        # if self.health == 0:
        #     return 0
        total_defense = 0

        if self.health == 0:
            return 0

        for armor in self.armors:
            armor_defense = armor.defend()
            total_defense += armor_defense

        return total_defense

    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the hero's health.
        # If the hero dies update number of deaths.
        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.kills += num_kills

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
        # for hero in self.heroes:
        #     if hero.name == name:
        #         heroExists = "The hero '{0}' exists".format(hero.name)
        #         return heroExists
        #     else:
        #         return "this hero doesn't exist"
        for index in range(len(self.heroes)):
            if self.heroes[index].name == name:
                return self.heroes[index]
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
            tempoVar = ""

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


class Arena():
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        # This method should allow a user to build team one.
        # print("TEAM ONE:")
        # self.team_one = Team(input("What's team one going to be named?"))
        # for i in range(self.team):
        #     print("Hero number {0} ".format(i))
        #     self.team_one.add_hero()
        # This method should allow a user to build team one.
        team_one = Team("Winners")
        print("TEAM ONE:")
        # Wonder Woman
        heroOne = Hero("Wonder Woman")
        team_one.add_hero(heroOne)
        print("Superhero 1: '{0}' is ready to fight!".format(heroOne.name))
        punchAbility = Ability("Punch", 500)
        heroOne.add_ability(punchAbility)
        # print(heroOne.abilities)
        lightArmor = Armor("light armor", 200)
        heroOne.add_armor(lightArmor)

        # Batman
        heroTwo = Hero("Batman")
        team_one.add_hero(heroTwo)
        print("Superhero 2: '{0}' is ready to fight! ".format(heroTwo.name))
        headBumb = Ability("Head bumb", 500)
        heroTwo.add_ability(headBumb)
        # print(team_one.heroes)

    def build_team_two(self):
        # This method should allow user to build team two.
        print("")
        print("TEAM TWO:")
        # self.team_one = Team(input("What's team two going to be named?"))
        # for i in range(self.team):
        #     print("Hero number {0} ".format(i))
        #     self.team_two.add_hero()
        # Superman
        heroFour = Hero("Superman")
        print("Superhero1: '{0}' is ready to fight: ".format(heroFour.name))
        superPunch = Ability("Superman punch", 700)
        heroFour.add_ability(superPunch)
        mediumArmor = Armor("mediumArmor", 200)
        heroFour.add_armor(mediumArmor)
        # print(heroFour)
        # Super Chicken
        heroFive = Hero("Super Chicken")
        print("Superhero2: '{0}' is ready to fight: ".format(heroFive.name))
        flapWings = Ability("Flap wings", 1200)
        heroFive.add_ability(flapWings)
        heavyArmor = Armor("heavy armor", 800)
        heroFive.add_armor(heavyArmor)

    def team_battle(self):
        # This method should continue to battle teams until one or both teams are dead.
        # battling = True
        # while battling == True:
        #     self.team_one.attack(self.team_two)
        #     self.team_two.attack(self.team_one)
        pass

    def show_stats(self):
        # This method should print out the battle statistics including each heroes kill/death ratio.
        pass


if __name__ == "__main__":
    arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()
    heroOneTeamOne = Hero("Jessica Jones", 100)
    heroTwoTeamOne = Hero("Daredevil", 100)
    teamWinners = Team("Team Winners")
    teamWinners.add_hero(heroOneTeamOne)
    teamWinners.add_hero(heroTwoTeamOne)
    print(teamWinners.find_hero("Daredevil"))  # Fix print statement and check for other heroes not just the first one
    teamWinners.view_all_heroes()

    # team two
    heroOneTeamTwo = Hero("batman", 100)
    heroTwoTeamTwo = Hero("joker", 100)
    # battle
