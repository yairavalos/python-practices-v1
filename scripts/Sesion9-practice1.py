### Interacción de clases
### Video juevos
### Vida y Ataques

# class Guerrero():
# class Arquero():

# damage = accuaracy * strength 
# accuaracy, damage, distance
# speed -> mts / sec ó resolucion


# Classes Definition:
# ------------------------------------------------------------------------------------------------------------

class Battle_Field():

    def __init__(self, large):
        self.large = large
        self.center = large/2

    def calculate_dis(self, pos1, pos2):
        self.distance = abs(pos2 - pos1)
        return self.distance

    def calculate_pos(self, pos, speed, direction):
        self.newPos = pos
        if direction == "right":
            self.newPos += speed
        elif direction == "left":
            self.newPos -= speed
        return self.newPos

    def display_battle_field(self, leftPos, rightPos):
        # Handle Positions
        leftPos = (round(leftPos,0)) + self.center
        rightPos = (round(rightPos,0)) + self.center
    
        # Represent Positions
        strChain = ""
        for step in range(self.large):
            if step == leftPos or step == rightPos:
                strChain += "|"
            elif step == self.center:
                strChain += "."
            else:
                strChain += "-"
        
        print("\n")
        print("[" + strChain + "]")

    
    def display_stamina(self, warrior1, warrior2):
        # calculate stamina from Warriors
        stamina1 = round((warrior1.live)*10,0)
        stamina2 = round((warrior2.live)*10,0)

        # represent stamina with strings
        strChainA = ""
        for step in range(10):
            if step < stamina1:
                strChainA += "+"
            else:
                strChainA += "-"

        strChainB = ""
        strChainC = ""

        for step in range(10):
            if step < stamina2:
                strChainB += "+"
            else:
                strChainC += "-"
        
        strChainD = ""

        for step in range(self.large - 22):
            strChainD += " "

        print("[" + strChainA + "]" + strChainD + "[" + strChainC + strChainB + "]")
        print("\n")
        print("\n")

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

    def engage(self, enemy, myBattleField: Battle_Field):
        self.enemy = enemy
        self.distance = myBattleField.calculate_dis(self.pos, self.enemy.pos)

    def endurance(self, myDamage):
        self.live -= self.live * myDamage
        self.strength -= self.strength * myDamage
        self.speed = self.speed * self.live * self.shield.calculate_agility()
        print(f'Endurace for {self.warrior_name} is live: {self.live * 100}%, strength: {self.strength * 100}%, speed: {self.speed} mts per advance')

    def advance(self, direction, myBattleField: Battle_Field):
        self.direction =  direction
        self.pos = myBattleField.calculate_pos(self.pos, self.speed, self.direction)
        self.distance = myBattleField.calculate_dis(self.pos, self.enemy.pos)
        print(f'Advance results for {self.warrior_name} are direction to the: {self.direction}, Position: {self.pos} mts from central position, Distance: {self.distance} mts against the enemy')

    def attack(self, enemy):
        self.attack_power = self.weapon.calculate_damage(self.distance,self.strength)
        print(f'{self.warrior_name} is attacking with {self.attack_power * 100}% of power with {self.weapon.weapon_name} as weapon') 
        enemy.deffense(self.attack_power)
        
    def deffense(self, attack_damage):
        self.protection = self.shield.calculate_coverage()
        print(f'Protecting {self.protection * 100}% to {self.warrior_name} with a {self.shield.size} shield has {attack_damage * self.protection * 100}% of damage as a result')
        self.endurance(attack_damage * self.protection)

    def report_status(self):
        print(f'Warrior:{self.warrior_name} | Weapon: {self.weapon.weapon_name} | Shield: {self.shield.size} | Position: {self.pos} mts | Direction: {self.direction}')
        self.endurance(0)


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
        return self.accuaracy * strength * (self.reach / distance)

    def report(self):
        print(f'Weapon Name: {self.weapon_name} | Accuaracy of: {self.accuaracy * 100}% | Reach: {self.reach} mts')


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
        print(f'Shield Size: {self.size} | Coverage of: {self.calculate_coverage() * 100}% | Agility of: {self.calculate_agility() * 100}%')


# Game Objects Initialization:
# ------------------------------------------------------------------------------------------------------------

theBattleField = Battle_Field(40)

weapon1 = Weapon("sword")
weapon2 = Weapon("archery")

shield1 = Shield("medium")
shield2 = Shield("small")

print("------------------------------------------------------------------------------------------------------------")
print("Warrior 1 Introduction:")
print("------------------------------------------------------------------------------------------------------------")
warrior1 = Warrior("knigth",weapon1,shield1, 0.95, 4, -15, "right")
warrior1.report_status()
warrior1.weapon.report()
warrior1.shield.report()
print("------------------------------------------------------------------------------------------------------------")
print("\n")

print("------------------------------------------------------------------------------------------------------------")
print("Warrior 2 Introduction:")
print("------------------------------------------------------------------------------------------------------------")
warrior2 = Warrior("elfo",weapon2,shield2, 0.75, 8, 17, "left")
warrior2.report_status()
warrior2.weapon.report()
warrior2.shield.report()
print("------------------------------------------------------------------------------------------------------------")
print("\n")
print("\n")

warrior1.engage(warrior2, theBattleField)
warrior2.engage(warrior1, theBattleField)

theBattleField.display_battle_field(warrior1.pos, warrior2.pos)
theBattleField.display_stamina(warrior1,warrior2)


# Main Program Flow:
# ------------------------------------------------------------------------------------------------------------

counter = 1
user_action = ""
user_direction = ""

while counter < 40 and warrior1.live > 0 and warrior2.live > 0:
    
    if counter %2 != 0:

        print("\n")
        print("Its Warrior 1 turn")
        user_action = input("What do you wanna do ?? 1 for advance, 2 for attack, 3 for report, 4 for Battle Field ---> ")

        if user_action == "1":
            
            user_direction = input("What direction do you wanna go ?? 1 for left or 2 for right ---> ")
            
            if user_direction == "1":
                print("Warrior 1 is advancing to the left")
                warrior1.advance("left",theBattleField)

            elif user_direction == "2":
                print("Warrior 1 is advancing to the right")
                warrior1.advance("right",theBattleField)

            else:
                print("Warrior 1 has lost his chance to advance")

        elif user_action == "2":
            print("Warrior 1 is ATTACKING !!! ")
            warrior1.attack(warrior2)

        elif user_action == "3":
            print("Warrior 1 Report ")
            warrior1.report_status()

        elif user_action == "4":
            theBattleField.display_battle_field(warrior1.pos, warrior2.pos)
            theBattleField.display_stamina(warrior1,warrior2)

        else:
            print("Warrior 1 has lost his chance for any action")


    if counter %2 == 0:
        
        print("\n")
        print("Its Warrior 2 turn")
        user_action = input("What do you wanna do ?? 1 for advance, 2 for attack, 3 for report, 4 for Battle Field ---> ")

        if user_action == "1":
            
            user_direction = input("What direction do you wanna go ?? 1 for left or 2 for right ---> ")
            
            if user_direction == "1":
                print("Warrior 2 is advancing to the left")
                warrior2.advance("left",theBattleField)

            elif user_direction == "2":
                print("Warrior 2 is advancing to the right")
                warrior2.advance("right",theBattleField)

            else:
                print("Warrior 2 has lost his chance to advance")

        elif user_action == "2":
            print("Warrior 2 is ATTACKING !!! ")
            warrior2.attack(warrior1)

        elif user_action == "3":
            print("Warrior 2 Report ")
            warrior2.report_status()

        elif user_action == "4":
            theBattleField.display_battle_field(warrior1.pos, warrior2.pos)
            theBattleField.display_stamina(warrior1,warrior2)

        else:
            print("Warrior 2 has lost his chance for any action")


    counter += 1


print("\n")
warrior1.report_status()

print("\n")
warrior2.report_status()

theBattleField.display_battle_field(warrior1.pos, warrior2.pos)
theBattleField.display_stamina(warrior1,warrior2)

if warrior1.live > warrior2.live:
    print(f'Warrior 1: {warrior1.warrior_name} its the WINNER !!! ')

if warrior2.live > warrior2.live:
    print(f'Warrior 2: {warrior1.warrior_name} its the WINNER !!! ')


print(" ------------- GAME OVER ---------------- ")
print("\n")
print("\n")
