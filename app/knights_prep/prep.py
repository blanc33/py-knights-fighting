class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protect = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
            self,
            name: str,
            hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.hp_effect = hp
        self.power_effect = power
        self.protect_effect = protection
