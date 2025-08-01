from Utils import *
from Comp import *
from SingleEnemies import SingleEnemyComps

priority_order = [3, 6, 4, 1, 2, 5] # 1-based

thisMode = "Nightmare Corridor"
enemy_names = ["Fractured Fool", "Abyssal Murmur", "Clawlossus",
               "Sky Serpent", "Nightmare Weaver", "Marsha"]

battles = [
    Comp(thisMode, f"Battle {i + 1} - {name}", SingleEnemyComps[name])
    for i, name in enumerate(enemy_names)
]

comp_list = CompList(battles, priority_order)
