### Interacción de clases
### Video juevos
### Vida y Ataques

# class Guerrero():
# class Arquero():

# damage = accuaracy * strength 
# accuaracy, damage, distance
# speed -> mts / sec ó resolucion

class Battle_Field():

    def __init__(self, large):
        self.large = large
        self.center = large/2

    def calculate_dis(self, pos1, pos2):
        self.distance = pos2 - pos1
        return self.distance

    def calculate_pos(self, pos, speed, direction):
        self.newPos = pos
        if direction == "right":
            self.newPos += speed
        elif direction == "left":
            self.newPos -= speed
        return self.newPos


class Warrior():

    def __init__(self, warrior_name, weapon, shield, strength, speed, initialPos, direction):
        self.live = 1.00
        self.warrior_name = warrior_name
        self.weapon = weapon
        self.shield = shield
        self.strength = strength
        self.speed = speed
        self.pos = initialPos
        self.direction = direction
        self.distance = 0
        self.enemy

    def engage(self, enemy: Warrior):
        self.enemy = enemy

    def endurance(self, myDamage):
        self.live -= self.live * myDamage
        self.strength *= self.live * self.shield.calculate_agility()
        self.speed *= self.live * self.shield.calculate_agility()

    def advance(self, direction, myBattleField: Battle_Field):
        self.direction =  direction
        self.pos = myBattleField.calculate_pos(self.pos, self.speed, self.direction)
        self.distance = myBattleField.calculate_dis(self.distance, self.enemy.distance)

    def attack(self, enemy: Warrior):
        enemy.deffense(self.weapon.calculate_damage())
        
    def deffense(self, attack_damage):
        self.endurance(self.shield.calculate_coverage(attack_damage))

    def report_status(self):
        pass


class Weapon():

    def __init__(self, weapon_name):
        self.weapon_name = weapon_name

        if self.weapon_name == "sword":
            self.accuaracy = 0.85
            self.reach = 1.5
        
        if self.weapon_name == "pike":
            self.accuaracy = 0.75
            self.reach = 2.5

        if self.weapon_name == "axe":
            self.accuaracy = 0.85
            self.reach = 1.0
        
        if self.weapon_name == "archery":
            self.accuaracy = 0.50
            self.reach = 15

    def calculate_damage(self, distance, strength):
        self.distance = distance
        self.strength = strength
        self.damage = self.accuaracy * self.strength * (self.reach / self.distance)
        return self.damage

    def report(self):
        pass


class Shield():

    def __init__(self, size):
        self.size = size

    def calculate_coverage(self):
        if self.size == "small":
            return 0.25
        if self.size == "medium":
            return 0.5
        if self.size == "large":
            return 0.75
        
    def calculate_agility(self):
        if self.size == "small":
            return 0.85
        if self.size == "medium":
            return 0.50
        if self.size == "large":
            return 0.25

    def report(self):
        pass


theBattleField = Battle_Field(200)

weapon1 = Weapon("sword")
weapon1.report()

weapon2 = Weapon("archery")
weapon2.report()

shield1 = Shield("medium")
shield1.report()

shield2 = Shield("small")
shield2.report()

warrior1 = Warrior("knigth",weapon1,shield1, 0.95, 1, -75)
warrior1.report_status()

warrior2 = Warrior("elfo",weapon2,shield2, 0.75, 2, 90)
warrior2.report_status()

warrior1.engage(warrior2)
warrior2.engage(warrior1)

counter = 1
user_action = ""
user_direction = ""

while counter < 20:

    if counter %2 != 0:

        print("Its Warrior 1 turn")
        user_action = input("What do you wanna do ?? 1 for advance or 2 for attack")

        if user_action == "1":
            
            user_direction = input("What direction do you wanna go ?? 1 for left or 2 for right")
            
            if user_direction == "1":
                print("Warrior 1 is advancing to the left")
                warrior1.advance("left")

            elif user_direction == "2":
                print("Warrior 1 is advancing to the right")
                warrior1.advance("right")

            else:
                print("Warrior 1 has lost his chance to advance")

        elif user_action == "2":
            print("Warrior 1 is ATTACKING !!! ")
            warrior1.attack(warrior2)

        else:
            print("Warrior 1 has lost his chance for any action")


    if counter %2 == 0:
        
        print("Its Warrior 2 turn")
        user_action = input("What do you wanna do ?? 1 for advance or 2 for attack")

        if user_action == "1":
            
            user_direction = input("What direction do you wanna go ?? 1 for left or 2 for right")
            
            if user_direction == "1":
                print("Warrior 2 is advancing to the left")
                warrior2.advance("left")

            elif user_direction == "2":
                print("Warrior 2 is advancing to the right")
                warrior2.advance("right")

            else:
                print("Warrior 2 has lost his chance to advance")

        elif user_action == "2":
            print("Warrior 2 is ATTACKING !!! ")
            warrior2.attack(warrior1)

        else:
            print("Warrior 2 has lost his chance for any action")


    counter += 1



