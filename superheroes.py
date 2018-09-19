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

class Hero(Ability):

	def __init__(self, name):
		self.name = name
		self.abilities = list()

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		total = 0
		for ab in self.abilities:
			total += Ability.attack(ab)
		return total

class Weapon(Ability):
    def attack(self):
    	randomVal = random.randint(0, self.attack_strength)
    	return randomVal

class Team(Hero):

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

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
    	
        


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    #print(hero1.attack())
    ability = Ability("Divine Speed", 300)
    hero1.add_ability(ability)
    #print(hero1.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero1.add_ability(new_ability)
    #print(hero1.attack())

    hero2 = Hero("Thor")
    ability2 = Ability("Flying Hammer", 500)
    hero2.add_ability(ability2)


    hero3 = Hero("Yosemite Sam")
    ability3 = Ability("Lasso", 600)
    hero3.add_ability(ability3)


    teamOfHeroes = Team("Losers")
    print(teamOfHeroes.add_hero(hero1))
    print(teamOfHeroes.add_hero(hero2))
    print(teamOfHeroes.add_hero(hero3))
    print(teamOfHeroes.find_hero("Yosemite Sam"))
    print(teamOfHeroes.remove_hero("Yosemite Sam"))
    #print(teamOfHeroes.remove_hero("Jabba")) # supposed to return 0
    print(teamOfHeroes.find_hero("Wonder Woman"))
    print(teamOfHeroes.find_hero("Yosemite Sam"))

    teamOfHeroes.view_all_heroes()
    


    

    
