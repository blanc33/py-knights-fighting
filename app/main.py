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


def battle(knights: dict) -> dict:
    for knight in knights.values():
        Knight(knight["name"], knight["power"], knight["hp"])

    for knight in knights.values():
        key = knight["name"].lower().replace(" ", "_")
        for arm in knight["armour"]:
            ar = Armour(**arm)
            Knight.knight_dict[key].get_armoured(ar)
        Knight.knight_dict[key].get_weapon(Weapon(**knight["weapon"]))
        if knight["potion"]:
            Knight.knight_dict[key].drink_potion(
                Potion(knight["potion"]["name"], **knight["potion"]["effect"])
            )

    knights = Knight.knight_dict
    knights["lancelot"].hp -= (knights["mordred"].power
                               - knights["lancelot"].protection)
    knights["mordred"].hp -= (knights["lancelot"].power
                              - knights["mordred"].protection)
    if knights["lancelot"].hp <= 0:
        knights["lancelot"].hp = 0
    if knights["mordred"].hp <= 0:
        knights["mordred"].hp = 0

    knights["arthur"].hp -= (knights["red_knight"].power
                             - knights["arthur"].protection)
    knights["red_knight"].hp -= (knights["arthur"].power
                                 - knights["red_knight"].protection)
    if knights["arthur"].hp <= 0:
        knights["arthur"].hp = 0
    if knights["red_knight"].hp <= 0:
        knights["red_knight"].hp = 0

    return \
        {
            knights["lancelot"].name: knights["lancelot"].hp,
            knights["arthur"].name: knights["arthur"].hp,
            knights["mordred"].name: knights["mordred"].hp,
            knights["red_knight"].name: knights["red_knight"].hp
        }


print(battle(KNIGHTS))
