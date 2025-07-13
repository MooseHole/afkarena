from Utils import *
from Comp import *
from Hero import Hero as h

priority_order = [1, 2, 3] # 1-based

# From https://afk.guide/dragonforge-trials-guide/
recommended_comps_per_battle = [
    # Battle 1
    [   [h.Cassius, h.Pulina, h.ASafiya, h.Nyla, h.Jerome],
        [h.Cassius, h.Pulina, h.ASafiya, h.Melion, h.Lan],
        [h.ASafiya, h.Cassius, h.Numisu, h.Villanelle, h.Lan],
    ] +
    expand_team([h.Lucilla, [h.AShemira, h.Talene], [h.Silas, h.Liberta], h.Ivan, h.DGwyneth]) +
    [   [h.Alna, h.Cassius, h.Silas, h.Pulina, h.ASafiya],
        [h.Lucilla, h.AShemira, h.Liberta, h.Ivan, h.DGwyneth],
        [h.Pulina, h.Nyla, h.Cassius, h.ASafiya, h.Emilia],
    ] + 
    expand_team([h.Veithael, h.AShemira, [h.Ivan, h.Emilia], [h.Ivan, h.Emilia], h.DGwyneth]),

    # Battle 2
    expand_team([h.AShemira, h.AAthalia, h.DGwyneth, [h.Emilia, h.Jerome], h.Ivan]) +
         [  [h.AShemira, h.Ivan, h.DGwyneth, h.Lavatune, h.Pulina],
          [h.Alna, h.Cassius, h.Liberta, h.Pulina, h.Nevanthi],
          [h.Nyla, h.Alna, h.Pulina, h.Atheus, h.ASafiya],
          [h.Lucilla, h.AShemira, h.Robin_Hood, h.Nyla, h.Liberta],
          [h.Pulina, h.ABrutus, h.Nyla, h.Cassius, h.ASafiya],
          [h.AShemira, h.Lucilla, h.DGwyneth, h.Liberta, h.Ivan],
          [h.Alna, h.Cassius, h.Liberta, h.Pulina, h.Nevanthi],
          [h.Pulina, h.Cassius, h.ASafiya, h.Nyla, h.Nevanthi],
        ],
    

    # Battle 3
    expand_team([h.Lucilla, h.Hildwin, h.Liberta, [h.Gavus, h.Nyla], [h.Lavatune, h.Melion]]) +
             [  [h.AShemira, h.Hildwin, h.Nyla, h.Emilia, h.Jerome],
          [h.ALucius, h.Jerome, h.Eugene, h.Palmer, h.Hildwin],

        ] +
        expand_team([h.ALucius, h.Jerome, h.Gavus, [h.Palmer, h.Lavatune], h.Hildwin]) +
        [  [h.ASolise, h.Hildwin, h.Gavus, h.Eugene, h.Jerome],
          [h.Atheus, h.Jerome, h.ASafiya, h.Nyla, h.Hildwin],
          [h.Jerome, h.Hildwin, h.Eugene, h.Gavus, h.Lavatune],
        ],

]

# Deduplicate and validate
recommended_comps_per_battle = [
    deduplicate_and_validate_battle_comps(battle)
    for battle in recommended_comps_per_battle
]

thisMode = "Dragon Forge Stage 9"
battles = [ Comp(thisMode, "Battle 1", recommended_comps_per_battle[0]),
            Comp(thisMode, "Battle 2", recommended_comps_per_battle[1]),
            Comp(thisMode, "Battle 3", recommended_comps_per_battle[2]),
          ]
