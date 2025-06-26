from Utils import FindBest
from MyHeroes import my_heroes
from NightmareCorridor import recommended_comps_per_battle as nightmareCorridorComps

if __name__ == "__main__":
    FindBest(nightmareCorridorComps, my_heroes)
