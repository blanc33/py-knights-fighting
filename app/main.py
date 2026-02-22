from app.knights_prep.knights import Knight
from app.knights_prep.prep import Armour, Weapon, Potion

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def fight(knight_a: Knight, knight_b: Knight) -> None:
    knight_a.hp -= max(0, knight_b.power - knight_a.protection)
    knight_b.hp -= max(0, knight_a.power - knight_b.protection)
    knight_a.hp = max(knight_a.hp, 0)
    knight_b.hp = max(knight_b.hp, 0)


def battle(knights: dict) -> dict[str, int]:
    prepared_knights: dict[str, Knight] = {}

    for key, knight_data in knights.items():
        current_knight = Knight(
            knight_data["name"], knight_data["power"], knight_data["hp"]
        )

        for armour_data in knight_data["armour"]:
            armour_part = Armour(**armour_data)
            current_knight.get_armoured(armour_part)

        current_knight.get_weapon(Weapon(**knight_data["weapon"]))

        if knight_data["potion"]:
            potion_effects = knight_data["potion"]["effect"]
            potion_obj = Potion(
                knight_data["potion"]["name"], **potion_effects
            )
            current_knight.drink_potion(potion_obj)

        prepared_knights[key] = current_knight

    # Simulate the fights
    fight(prepared_knights["lancelot"], prepared_knights["mordred"])
    fight(prepared_knights["arthur"], prepared_knights["red_knight"])

    return {knight.name: knight.hp for knight in prepared_knights.values()}
