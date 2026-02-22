from app.knights_prep.prep import Armour, Weapon, Potion


class Knight:
    knight_dict = {}

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour_list = []
        self.protection = 0
        self.weapon = None
        self.potion = None
        # Knight.knight_dict[self.name] = self
        # key = name.lower().replace(" ", "_")
        Knight.knight_dict[name.lower().replace(" ", "_")] = self

    def get_armoured(self, armour: "Armour") -> None:
        self.armour_list.append(armour)
        self.protection += armour.protect

    def get_weapon(self, weapon: "Weapon") -> None:
        self.weapon = weapon
        self.power += weapon.power

    def drink_potion(self, potion: "Potion") -> None:
        self.potion = potion
        self.hp += potion.hp_effect
        self.power += potion.power_effect
        self.protection += potion.protect_effect
