from Utils import *
from Comp import *

priority_order = [2, 5, 1, 4, 6, 3] # 1-based

# From https://afk.guide/nightmare-corridor-guide-teams/
recommended_comps_per_battle = [
    # Battle 1 – Astral Devourer
    expand_team(["Zohra", ["Melion", "Atheus", "Randle", "Lucilla", "Raine", "Mortas"], "Ivan", "Envydiel", ["Daemia", "ASafiya"]]) +
    expand_team([["Zohra", "Lucilla", "Rimuru", "Skylan", "Melion", "Knox"], "Sion", "Daemia", "Palmer", "Ivan"]) +
    expand_team(["Zohra", "Envydiel", "Ivan", ["Mortas", "Palmer", "Elijah-Lailah"], "Daemia"]) +
    expand_team(["Knox", "Rimuru", "Daemia", ["Palmer", "Liberta"], "ALyca"]) +
    [["Liberta", "ALyca", "Elijah-Lailah", "Rimuru", "Daemia"]] +
    expand_team([["ALyca", "ALucius"], "Knox", "Daemia", "Palmer", "Ivan"]) +
    expand_team(["Daemia", ["Lucilla", "Knox"], ["Liberta", "Palmer", "Lavatune"], "AAthalia", "Rimuru"]) +
    expand_team([["Palmer", "Lucilla"], "Zohra", ["Liberta", "Jerome", "Lucilla", "Ivan"], "Daemia", ["Knox", "AThoran"]]) +
    [   ["Lucilla", "Liberta", "Daemia", "Zohra", "Lady-Simona"],
        ["Daemia", "Skylan", "Liberta", "Lucilla", "Rimuru"],
        ["Skylan", "Lucilla", "Daemia", "Zohra", "ALyca"],
        ["Crassio", "Palmer", "Daemia", "Rimuru", "Lucilla"],
        ["Knox", "Lavatune", "Daemia", "Palmer", "Haelia"],
        ["AThoran", "Rimuru", "Liberta", "Daemia", "AShemira"],
    ],

    # Battle 2 – Fractured Fool
    expand_team(["Orthros", "Liberta", "Lucilla", "Knox", ["Haelia", "Shuna", "Rosaline", "Gavus", "Veithael"]]) +
    [   ["Orthros", "Jerome", "Knox", "Liberta", "Lucilla"],
        ["Shuna", "Knox", "Liberta", "Lysander", "Orthros"],
        ["AAthalia", "AThoran", "ASafiya", "Lucilla", "Lysander"],
        ["AThane", "Lan", "Haelia", "Veithael", "Aurelia"],
        ["Warek", "Lan", "AThane", "Veithael", "Aurelia"],] +
    expand_team([["Lan", "Lavatune"], "Jerome", ["Raine", "Lorsan", "AThoran", "Veithael"], ["Vika", "AThane"], "Rosaline"]) +
    [   ["Lavatune", "Rosaline", "Lorsan", "Vika", "Lady-Simona"],
        ["Vika", "Lucilla", "Rimuru", "Lavatune", "Liberta"],
        ["Vika", "Lavatune", "Rosaline", "Anasta", "Raoul"],] +
    expand_team(["Rem", "ASolise", "Randle", ["Misha", "AThoran"], ["Naroko", "Numisu", "AThoran"]]) +
    expand_team(["Trishea", "Baden", "Elijah-Lailah", ["Villanelle", "Hodgkin"], "Aurelia"]) +
    [   ["Jerome", "Lavatune", "Raine", "ABelinda", "Rosaline"],
        ["ABelinda", "Liberta", "Raine", "Lavatune", "Knox"],
        ["Naroko", "Lucilla", "Knox", "Liberta", "Ivan"],
        ["Sion", "Lyca", "ASafiya", "Villanelle", "Naroko"], ],

    # Battle 3 – Abyssal Murmur
    expand_team([["Randle", "Adrian-Elyse", "Lan"], ["Hodgkin", "Melion", "Lavatune"], "Rimuru", "Sion", "Misha"]) +
    expand_team([["Envydiel", "Zohra"], ["Randle", "AThoran", "Raine"], ["Hodgkin", "Palmer", "Velufira"], ["Misha", "Saurus", "Lavatune", "Knox"], ["Rimuru", "Raine", "Jerome", "Estrilda", "Saurus", "Silas"]]) +
    [   ["Melion", "Lavatune", "Rosaline", "Haelia", "Rimuru"],
        ["Lan", "AThane", "AEstrilda", "Jerome", "Raine"],] +
    expand_team(["Trishea", "Baden", "Elijah-Lailah", ["Knox", "Nevanthi", "Naroko", "Lavatune", "AThoran"], ["Aurelia", "Nevanthi"]]) +
    expand_team(["Rem", "ASolise", ["Naroko", "Numisu", "AThoran"], "Misha", "Randle"]) +
    expand_team(["AEironn", "Randle", "Misha", ["Knox", "Rimuru"], "Hodgkin"]),

    # Battle 4 - Clawlossus
    expand_team(["Jerome", ["Lavatune", "Lan"], "Raine", ["Marcille", "DGwyneth"], "Rosaline"]) +
    expand_team(["Marcille", ["Aurelia", "Velufira"], ["Silas", "Elijah-Lailah"], "Lavatune", ["Laios", "Randle", "Velufira"]]) +
    expand_team(["Aurelia", "Lavatune", ["Rosaline", "Raine"], "Marcille", "Velufira"]) +
    [   ["Randle", "AThoran", "Velufira", "Lysander", "DGwyneth"],
        ["AThoran", "AAthalia", "Randle", "Lysander", "Velufira"],
        ["Sion", "Velufira", "Rimuru", "Misha", "Randle"],
        ["Randle", "ABelinda", "Jerome", "Lavatune", "Rosaline"],
        ["Envydiel", "Jerome", "Raine", "Velufira", "Lan"],] +
    expand_team(["Envydiel", "Raine", "Velufira", ["Atheus", "Lan"], ["Rimuru", "Silas"]]) +
    [   ["Envydiel", "Randle", "Rimuru", "Misha", "Hodgkin"],] +
    expand_team(["Trishea", "Baden", "Aurelia", ["Lavatune", "Knox", "Liberta", "Hodgkin"], "Elijah-Lailah"]),

    # Battle 5 - Sky Serpent
    expand_team(["Orthros", ["Laios", "Velufira", "Lucilla", "ASolise", "Leviathan", "Kregor"], ["Knox", "Velufira"], "Palmer", "Liberta"]) +
    [   ["Randle", "Misha", "Silas", "ASolise", "Hodgkin"],] +
    expand_team([["ALyca", "Rimuru", "Envydiel"], "Randle", ["Silas", "Rimuru", "Ivan"], "Misha", "Hodgkin"]) +
    [   ["Jerome", "Randle", "ALyca", "Misha", "ASolise"],
        ["Jerome", "Sion", "Villanelle", "Shuna", "Knox"],],
        
    # Battle 6 - Nightmare Weaver
    expand_team([["Leviathan", "Adrian-Elyse", "AEstrilda", "Lan"], ["Misha", "Lan"], "Rimuru", "Sion", ["Melion", "Lan"]]) +
    [   ["ALyca", "Melion", "Misha", "Sion", "Rimuru"],] +
    expand_team(["Envydiel", "AThoran", "Lan", ["Melion", "Velufira"], "Laios"]) +
    [   ["AThoran", "Sion", "Lan", "Laios", "Shuna"],
        ["Lan", "Bronn", "Sion", "Palmer", "Melion"],
        ["Envydiel", "Laios", "Raine", "Lysander", "Lan"],],
]

# Deduplicate and validate
recommended_comps_per_battle = [
    deduplicate_and_validate_battle_comps(battle)
    for battle in recommended_comps_per_battle
]

thisMode = "Nightmare Corridor"
battles = [ Comp(thisMode, "Battle 1 - Astral Devourer", recommended_comps_per_battle[0]),
            Comp(thisMode, "Battle 2 - Fractured Fool", recommended_comps_per_battle[1]),
            Comp(thisMode, "Battle 3 - Abyssal Murmur", recommended_comps_per_battle[2]),
            Comp(thisMode, "Battle 4 - Clawlossus", recommended_comps_per_battle[3]),
            Comp(thisMode, "Battle 5 - Sky Serpent", recommended_comps_per_battle[4]),
            Comp(thisMode, "Battle 6 - Nightmare Weaver", recommended_comps_per_battle[5]) ]
