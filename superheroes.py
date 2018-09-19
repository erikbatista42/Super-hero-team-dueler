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

    def __init__(self,team_name):
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
	
def attack(self, other_team):
	# This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
    # It should call add_kill() on each hero with the number of kills made.
	self.other_team = other_team
	
def defend(self, damage_amt):
	#This method should calculate our team's total defense.
    #Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
    # Return number of heroes killed in attack.
	self.damage_amt = damage_amt

def deal_damage(self, damage):
	# Divide the total damage amongst all heroes.
    # Return the number of heros that died in attack.
	self.damage = damage

def revive_heroes(self, health = 100):
	# This method should reset all heroes health to their original starting value.
	self.health = health

def stats(self):
	print(123)
	# This method should print the ratio of kills/deaths for each member of the team to the screen. 
	# This data must be output to the terminal.

def update_kills(self):
	print(123)
	# this method should update each hero when there is a team kill


if __name__ == "__main__":

	# Wonder Woman
	heroOne = Hero("Wonder Woman")
	print(heroOne.name)
	punchAbility = Ability("Punch", 500)
	heroOne.add_ability(punchAbility)
	print("Wonder Woman is attacking:")
	print(heroOne.attack())

	# Superman
	heroTwo = Hero("Superman")
	print(heroTwo.name)
	superPunch = Ability("Superman Punch", 700)
	heroTwo.add_ability(superPunch)
	print("Superman is attacking:")
	print(heroTwo.attack())

	# Batman
	heroThree = Hero("Batman")
	print(heroThree.name)
	headBumb = Ability("Head bumb", 500)
	heroThree.add_ability(headBumb)
	print("Batman is attacking:")
	print(heroThree.attack())

	# Super Chicken
	heroFour = Hero("Super Chicken")
	flapWings = Ability("Flap wings", 8000)
	heroFour.add_ability(flapWings)
	print("Super Chicken is attacking:")
	print(heroFour.attack())

	# Shotgun weapon
	weaponOne = Weapon("Shotgun", 1000)
	print(weaponOne.name)
	print(weaponOne.attack_strength)
	print("Weapons is attacking:")
	print(weaponOne.attack())

	# Losers Team
	teamOne = Team("Losers")
	teamOne.add_hero(heroTwo)
	teamOne.add_hero(heroThree)
	teamOne.view_all_heroes()

	# Winners Team
	teamTwo = Team("Winners")
	teamTwo.add_hero(heroOne)
	teamTwo.add_hero(heroFour)
	teamTwo.view_all_heroes()
    


    

    
