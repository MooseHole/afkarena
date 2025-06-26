from Utils import FindBest
from MyHeroes import my_heroes
from NightmareCorridor import battles as nightmareCorridorBattles
from NightmareCorridor import priority_order as NCp
from DragonForge9 import battles as DF9Battles, priority_order as DF9p

if __name__ == "__main__":
    FindBest(nightmareCorridorBattles, my_heroes, NCp)
    FindBest(DF9Battles, my_heroes, DF9p)
