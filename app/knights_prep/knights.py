from __future__ import annotations
from app.knights_prep.prep import Armour, Weapon, Potion


class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour_list: list[Armour] = []
        self.protection = 0
        self.weapon: Weapon | None = None
        self.potion: Potion | None = None

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
