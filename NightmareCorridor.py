from Utils import *
from Comp import *
from Hero import Hero as h

priority_order = [3, 4, 5, 6, 1, 2] # 1-based

# From https://afk.guide/nightmare-corridor-guide-teams/
recommended_comps_per_battle = [
    # Battle 1 – Astral Devourer
    expand_team([h.Zohra, [h.Melion, h.Atheus, h.Randle, h.Lucilla, h.Raine, h.Mortas], h.Ivan, h.Envydiel, [h.Daemia, h.ASafiya]]) +
    expand_team([[h.Zohra, h.Lucilla, h.Rimuru, h.Skylan, h.Melion, h.Knox], h.Sion, h.Daemia, h.Palmer, h.Ivan]) +
    expand_team([h.Zohra, h.Envydiel, h.Ivan, [h.Mortas, h.Palmer, h.Elijah_Lailah], h.Daemia]) +
    expand_team([h.Knox, h.Rimuru, h.Daemia, [h.Palmer, h.Liberta], h.ALyca]) +
    [[h.Liberta, h.ALyca, h.Elijah_Lailah, h.Rimuru, h.Daemia]] +
    expand_team([[h.ALyca, h.ALucius], h.Knox, h.Daemia, h.Palmer, h.Ivan]) +
    expand_team([h.Daemia, [h.Lucilla, h.Knox], [h.Liberta, h.Palmer, h.Lavatune], h.AAthalia, h.Rimuru]) +
    expand_team([[h.Palmer, h.Lucilla], h.Zohra, [h.Liberta, h.Jerome, h.Lucilla, h.Ivan], h.Daemia, [h.Knox, h.AThoran]]) +
    [   [h.Lucilla, h.Liberta, h.Daemia, h.Zohra, h.Lady_Simona],
        [h.Daemia, h.Skylan, h.Liberta, h.Lucilla, h.Rimuru],
        [h.Skylan, h.Lucilla, h.Daemia, h.Zohra, h.ALyca],
        [h.Crassio, h.Palmer, h.Daemia, h.Rimuru, h.Lucilla],
        [h.Knox, h.Lavatune, h.Daemia, h.Palmer, h.Haelia],
        [h.AThoran, h.Rimuru, h.Liberta, h.Daemia, h.AShemira],
    ],

    # Battle 2 – Fractured Fool
    expand_team([h.Orthros, h.Liberta, h.Lucilla, h.Knox, [h.Haelia, h.Shuna, h.Rosaline, h.Gavus, h.Veithael]]) +
    [   [h.Orthros, h.Jerome, h.Knox, h.Liberta, h.Lucilla],
        [h.Shuna, h.Knox, h.Liberta, h.Lysander, h.Orthros],
        [h.AAthalia, h.AThoran, h.ASafiya, h.Lucilla, h.Lysander],
        [h.AThane, h.Lan, h.Haelia, h.Veithael, h.Aurelia],
        [h.Warek, h.Lan, h.AThane, h.Veithael, h.Aurelia],] +
    expand_team([[h.Lan, h.Lavatune], h.Jerome, [h.Raine, h.Lorsan, h.AThoran, h.Veithael], [h.Vika, h.AThane], h.Rosaline]) +
    [   [h.Lavatune, h.Rosaline, h.Lorsan, h.Vika, h.Lady_Simona],
        [h.Vika, h.Lucilla, h.Rimuru, h.Lavatune, h.Liberta],
        [h.Vika, h.Lavatune, h.Rosaline, h.Anasta, h.Raoul],] +
    expand_team([h.Rem, h.ASolise, h.Randle, [h.Misha, h.AThoran], [h.Naroko, h.Numisu, h.AThoran]]) +
    expand_team([h.Trishea, h.Baden, h.Elijah_Lailah, [h.Villanelle, h.Hodgkin], h.Aurelia]) +
    [   [h.Jerome, h.Lavatune, h.Raine, h.ABelinda, h.Rosaline],
        [h.ABelinda, h.Liberta, h.Raine, h.Lavatune, h.Knox],
        [h.Naroko, h.Lucilla, h.Knox, h.Liberta, h.Ivan],
        [h.Sion, h.Lyca, h.ASafiya, h.Villanelle, h.Naroko], ],

    # Battle 3 – Abyssal Murmur
    expand_team([[h.Randle, h.Adrian_Elyse, h.Lan], [h.Hodgkin, h.Melion, h.Lavatune], h.Rimuru, h.Sion, h.Misha]) +
    expand_team([[h.Envydiel, h.Zohra], [h.Randle, h.AThoran, h.Raine], [h.Hodgkin, h.Palmer, h.Velufira], [h.Misha, h.Saurus, h.Lavatune, h.Knox], [h.Rimuru, h.Raine, h.Jerome, h.Estrilda, h.Saurus, h.Silas]]) +
    [   [h.Melion, h.Lavatune, h.Rosaline, h.Haelia, h.Rimuru],
        [h.Lan, h.AThane, h.AEstrilda, h.Jerome, h.Raine],] +
    expand_team([h.Trishea, h.Baden, h.Elijah_Lailah, [h.Knox, h.Nevanthi, h.Naroko, h.Lavatune, h.AThoran], [h.Aurelia, h.Nevanthi]]) +
    expand_team([h.Rem, h.ASolise, [h.Naroko, h.Numisu, h.AThoran], h.Misha, h.Randle]) +
    expand_team([h.AEironn, h.Randle, h.Misha, [h.Knox, h.Rimuru], h.Hodgkin]),

    # Battle 4 - Clawlossus
    expand_team([h.Jerome, [h.Lavatune, h.Lan], h.Raine, [h.Marcille, h.DGwyneth], h.Rosaline]) +
    expand_team([h.Marcille, [h.Aurelia, h.Velufira], [h.Silas, h.Elijah_Lailah], h.Lavatune, [h.Laios, h.Randle, h.Velufira]]) +
    expand_team([h.Aurelia, h.Lavatune, [h.Rosaline, h.Raine], h.Marcille, h.Velufira]) +
    [   [h.Randle, h.AThoran, h.Velufira, h.Lysander, h.DGwyneth],
        [h.AThoran, h.AAthalia, h.Randle, h.Lysander, h.Velufira],
        [h.Sion, h.Velufira, h.Rimuru, h.Misha, h.Randle],
        [h.Randle, h.ABelinda, h.Jerome, h.Lavatune, h.Rosaline],
        [h.Envydiel, h.Jerome, h.Raine, h.Velufira, h.Lan],] +
    expand_team([h.Envydiel, h.Raine, h.Velufira, [h.Atheus, h.Lan], [h.Rimuru, h.Silas]]) +
    [   [h.Envydiel, h.Randle, h.Rimuru, h.Misha, h.Hodgkin],] +
    expand_team([h.Trishea, h.Baden, h.Aurelia, [h.Lavatune, h.Knox, h.Liberta, h.Hodgkin], h.Elijah_Lailah]),

    # Battle 5 - Sky Serpent
    expand_team([h.Orthros, [h.Laios, h.Velufira, h.Lucilla, h.ASolise, h.Leviathan, h.Kregor], [h.Knox, h.Velufira], h.Palmer, h.Liberta]) +
    [   [h.Randle, h.Misha, h.Silas, h.ASolise, h.Hodgkin],] +
    expand_team([[h.ALyca, h.Rimuru, h.Envydiel], h.Randle, [h.Silas, h.Rimuru, h.Ivan], h.Misha, h.Hodgkin]) +
    [   [h.Jerome, h.Randle, h.ALyca, h.Misha, h.ASolise],
        [h.Jerome, h.Sion, h.Villanelle, h.Shuna, h.Knox],],
        
    # Battle 6 - Nightmare Weaver
    expand_team([[h.Leviathan, h.Adrian_Elyse, h.AEstrilda, h.Lan], [h.Misha, h.Lan], h.Rimuru, h.Sion, [h.Melion, h.Lan]]) +
    [   [h.ALyca, h.Melion, h.Misha, h.Sion, h.Rimuru],] +
    expand_team([h.Envydiel, h.AThoran, h.Lan, [h.Melion, h.Velufira], h.Laios]) +
    [   [h.AThoran, h.Sion, h.Lan, h.Laios, h.Shuna],
        [h.Lan, h.Bronn, h.Sion, h.Palmer, h.Melion],
        [h.Envydiel, h.Laios, h.Raine, h.Lysander, h.Lan],],
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
