# This code defines a simple battle simulation between two Pokemon. 
# It includes an entity class that represents a generic entity with health points (HP) and attack power, 
# and a pokemon class that inherits from entity and adds a type attribute. 
# The battle function simulates a fight between two Pokemon, where they take turns attacking each other
# until one of them faints (HP drops to 0 or below). Finally, it creates two Pokemon instances and starts the battle.

class entity:
    def __init__(self, name, hp, attack): 
        self.name = name
        self.hp = hp
        self.attack = attack

# The __init__ method is a constructor that initializes the name, hp, and attack attributes 
# of the entity class when an instance is created.

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self, other):
        other.take_damage(self.attack)

# The is_alive method checks if the entity is still alive (HP greater than 0).
# The take_damage method reduces the entity's HP by the specified damage amount and ensures it doesn't drop below 0.
# The deal_damage method allows one entity to attack another by calling 
# the take_damage method on the other entity with the attack power of the attacking entity.

class pokemon(entity):
    def __init__(self, name, hp, attack, type):
        super().__init__(name, hp, attack)
        self.type = type

# The pokemon class inherits from the entity class and adds an additional attribute called type.

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}, Type: {self.type})"
    
    # The __str__ method provides a string representation of the pokemon instance,
    # which includes its name, HP, attack power, and type.

def battle(pokemon1, pokemon2):
    print(f"Battle Start: {pokemon1} vs {pokemon2}")
    while pokemon1.is_alive() and pokemon2.is_alive():
        pokemon1.deal_damage(pokemon2)
        print(f"{pokemon1.name} attacks {pokemon2.name}! {pokemon2.name} HP is now {pokemon2.hp}")
        if not pokemon2.is_alive():
            print(f"{pokemon2.name} has fainted! {pokemon1.name} wins!")
            break
        pokemon2.deal_damage(pokemon1)
        print(f"{pokemon2.name} attacks {pokemon1.name}! {pokemon1.name} HP is now {pokemon1.hp}")
        if not pokemon1.is_alive():
            print(f"{pokemon1.name} has fainted! {pokemon2.name} wins!")
            break

# The battle function simulates a fight between two Pokemon. It continues until one of the Pokemon faints (HP drops to 0 or below).
# During each turn, one Pokemon attacks the other, and the HP of the attacked Pokemon is
# updated accordingly. The function also prints the status of the battle after each attack.

pokemon1 = pokemon("Pikachu", 100, 20, "Electric")
pokemon2 = pokemon("Charmander", 120, 15, "Fire")
battle(pokemon1, pokemon2)
