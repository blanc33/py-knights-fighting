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
    knights_str_list = list(KNIGHTS)

    for i, knight in enumerate(knights.values()):
        current_kn = Knight(knight["name"], knight["power"], knight["hp"])
        for arm in knight["armour"]:
            ar = Armour(**arm)
            current_kn.get_armoured(ar)
        current_kn.get_weapon(Weapon(**knight["weapon"]))
        if knight["potion"]:
            current_kn.drink_potion(
                Potion(knight["potion"]["name"], **knight["potion"]["effect"])
            )
        locals()[knights_str_list[i]] = current_kn

    print(locals())

    for k1, k2 in [("lancelot", "mordred"), ("arthur", "red_knight")]:
        locals()[k1].hp -= (locals()[k2].power
                            - locals()[k1].protection)
        locals()[k2].hp -= (locals()[k1].power
                            - locals()[k2].protection)
        if locals()[k1].hp <= 0:
            locals()[k1].hp = 0
        if locals()[k2].hp <= 0:
            locals()[k2].hp = 0

    return \
        {
            locals()["lancelot"].name: locals()["lancelot"].hp,
            locals()["arthur"].name: locals()["arthur"].hp,
            locals()["mordred"].name: locals()["mordred"].hp,
            locals()["red_knight"].name: locals()["red_knight"].hp
        }


print(battle(KNIGHTS))
