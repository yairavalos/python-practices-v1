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

    def calculate_dis(self, warrior: Warrior):
        pass

class Warrior():

    def __init__(self, weapon, shield, strength, speed, pos):
        self.live = 100
        self.weapon = weapon
    
    def advance(self, enemy):
        pass

    def attack(self, enemy):
        pass

    def deffense(self, enemy):
        pass


class Weapon():

    def __init__(self, weapon_name, accuaracy, strength, reach):
        self.weapon_name = weapon_name
        self.accuaracy = accuaracy
        self.strength = strength
        self.reach = reach

    def calculate_damage(self, distance):
        self.distance = distance
        if self.reach == "long":
            self.damage = self.accuaracy * self.strength * self.distance
        elif self.reach == "short":
            self.damage = self.accuaracy * self.strength / self.distance


class Shield():

    def __init__(self, size):
        self.size = size

    def calculate_coverage(self, damage):
        if self.size == "small":
            return damage * 0.25
        if self.size == "medium":
            return damage * 0.5
        if self.size == "large":
            return damage * 0.75


