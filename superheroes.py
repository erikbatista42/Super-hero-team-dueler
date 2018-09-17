import random

class Ability:

	def __init__(self, name, attack_strength):
		self.name = name
		self.attack_strength = attack_strength

	def attack(self):
		highestAttackVal = 800
		lowestAttackVal = highestAttackVal // 2
		randomAttackVal = random.randint(0, highestAttackVal)
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



if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

    
